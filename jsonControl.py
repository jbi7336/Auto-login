import json
import os

# Json 읽어서 반환
def read_json():
    account = {
        "account": [
        ]
    }

    try:
        with open("./resource/id.json", "r", encoding="UTF8") as f:
            account = json.load(f)
    except FileNotFoundError:
        print("No file")

    return account

# 입력받은 정보를 json 형태로 만들어서 반환
def input_account(id, pw, job, platform):
    temp = [False, {
        "PLATFORM": platform,
        "ID": id,
        "PW": pw,
        "JOB": job
    }]

    return temp

# listView 모델이 가진 데이터프레임을 json 형태의 파일로 저장
def make_json(jsonObject):
    try:
        with open("./resource/id.json", "w", encoding="UTF8") as f:
            json.dump(jsonObject, f, indent="\t")
    except FileNotFoundError:
        os.makedirs("./resource")