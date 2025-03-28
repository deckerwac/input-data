import json
import os


def collect_data():
    person = {"name": "", "dob": "", "address": "", "email": ""}

    print("\n>.<\n")

    person["name"] = input("[+] 姓名: ")
    person["dob"] = input("[+] 出生日期: ")
    person["address"] = input("[+] 地址: ")
    person["email"] = input("[+] 电子邮件: ")

    return person


def load_existing_data(filename='/result/result.json'):  # 设置保存位置
    if os.path.exists(filename):
        with open(filename, 'r') as json_file:
            data = json.load(json_file)
            return data
    return []


def save_data_to_json(data, filename='/result/result.json'):  # 设置保存位置
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=1)
    print(f"\n➜ 文件夹位置 : {filename}\n")


def main():
    existing_data = load_existing_data()
    new_data = collect_data()

    existing_data.append(new_data)

    save_data_to_json(existing_data)


if __name__ == "__main__":
    main()

