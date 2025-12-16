^Xceptor/(Precis/input/[^/]+|V3(/ghss/(?!HKHIFSF)[^/]+|/[^/]+))$

import boto3
from datetime import datetime, timedelta, timezone

s3 = boto3.client("s3")

BUCKET = "your-bucket"
YEAR_PREFIX = "2025"  # 或根据今天动态生成


def list_latest_object(bucket, prefix):
    """
    只获取 prefix 下最新的 1 个对象。
    若没有对象则返回 None.
    """
    resp = s3.list_objects_v2(
        Bucket=bucket,
        Prefix=prefix,
        MaxKeys=1
    )
    if resp.get("KeyCount", 0) == 0:
        return None

    # S3 默认按字典顺序，最新文件未必是第一个，但一般你的路径带时间戳，所以无问题。
    return resp["Contents"][0]


def utc_to_hkt(dt_utc):
    return dt_utc.astimezone(timezone(timedelta(hours=8)))


def check_files_arrived():
    now_hkt = datetime.now(timezone(timedelta(hours=8)))
    today_hkt = now_hkt.date()

    # 今日 UTC 与 昨日 UTC 日期
    today_utc_date = (now_hkt - timedelta(hours=8)).date()
    yesterday_utc_date = today_utc_date - timedelta(days=1)

    # 你的 S3 路径结构需要确认一下是否为： 2025/yyyy-mm-dd/
    today_prefix = f"{YEAR_PREFIX}/{today_utc_date}/"
    yesterday_prefix = f"{YEAR_PREFIX}/{yesterday_utc_date}/"

    print("检查路径: ", today_prefix, yesterday_prefix)

    # 获取两个目录中最新文件
    latest_today = list_latest_object(BUCKET, today_prefix)
    latest_yesterday = list_latest_object(BUCKET, yesterday_prefix)

    # HKT 时间窗口（第一批 04:00 - 07:00）
    start_window = datetime.combine(today_hkt, datetime.min.time(), tzinfo=timezone(timedelta(hours=8))) \
                    + timedelta(hours=4)
    end_window = datetime.combine(today_hkt, datetime.min.time(), tzinfo=timezone(timedelta(hours=8))) \
                    + timedelta(hours=7)

    print(f"HKT 时间窗口: {start_window} - {end_window}")

    # 收集候选文件时间（HKT）
    candidate_times = []

    for obj in [latest_today, latest_yesterday]:
        if obj:
            lm_utc = obj["LastModified"]
            lm_hkt = utc_to_hkt(lm_utc)
            candidate_times.append(lm_hkt)
            print("候选文件时间(HKT):", lm_hkt)

    # 如果两个 prefix 都没文件
    if not candidate_times:
        print("没有任何文件，判定为延迟")
        return False

    # 判断是否落在窗口
    for t in candidate_times:
        if start_window <= t <= end_window:
            print("文件已正常到达 ✔")
            return True

    print("文件未在窗口内到达 ❌")
    return False


if __name__ == "__main__":
    arrived = check_files_arrived()
    print("最终结果:", arrived)
