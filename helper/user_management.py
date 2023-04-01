import os
import json

user_data_dir = "user_data"


def save_message(sender_id: str, role: str, message: str) -> None:
    message_data = {'role': role, 'content': message}
    file_path = os.path.join(user_data_dir, f'{sender_id}_messages.txt')

    with open(file_path, 'a') as f:
        f.write(json.dumps(message_data) + '\n')


def get_user_messages(sender_id: str) -> list:
    message_history = []
    file_path = os.path.join(user_data_dir, f'{sender_id}_messages.txt')

    if os.path.isfile(file_path):
        with open(file_path, 'r') as f:
            lines = f.readlines()
            for line in lines:
                message_history.append(json.loads(line.strip()))

    return message_history


def limit_requests(sender_id: str) -> bool:
    request_count_file = os.path.join(user_data_dir, f'{sender_id}_requests.txt')

    if os.path.isfile(request_count_file):
        with open(request_count_file, 'r') as f:
            count = int(f.read().strip())
    else:
        count = 0

    if count >= 100:
        return True

    with open(request_count_file, 'w') as f:
        f.write(str(count + 1))

    return False
