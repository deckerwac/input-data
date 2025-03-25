import json
import os


def collect_data():
    person = {"name": "", "dob": "", "address": "", "email": ""}

    print("\n>.<\n")

    person["name"] = input("$ Name: ")
    person["dob"] = input("$ DOB: ")
    person["address"] = input("$ Address: ")
    person["email"] = input("$ Email: ")

    return person


def load_existing_data(filename='/result/'):  # 设置保存位置
    if os.path.exists(filename):
        with open(filename, 'r') as json_file:
            data = json.load(json_file)
            return data
    return []


def save_data_to_json(data, filename='/result/'):  # 设置保存位置
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

