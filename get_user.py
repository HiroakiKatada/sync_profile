import os
import requests

# トークンの設定
token = os.environ.get('SLACK_TOKEN')

# 全ユーザーのIDを取得し、最初の20人のユーザーを選択
# response = requests.get('https://slack.com/api/users.list', headers={'Authorization': f'Bearer {token}'})
# user_ids = [
#     user['id'] for user in response.json()['members']
#     if not user.get('deleted') and not user.get('is_bot') and user['id'] != 'USLACKBOT'
# ][:20]

# テスト〜
user_ids = ['U05098X3QKF']

# ファイルに書き出し
with open('user_profiles.txt', 'w') as file:
    for user_id in user_ids:
        profile_response = requests.get(f'https://slack.com/api/users.profile.get?user={user_id}', headers={'Authorization': f'Bearer {token}'})
        profile_data = profile_response.json()

        if 'profile' in profile_data:
            # 変数に格納
            real_name = profile_data['profile'].get('real_name', 'No Name Provided')
            local_gov = profile_data['profile']['fields'].get('Xf06AC136N0N', {}).get('value', '')
            port = profile_data['profile']['fields'].get('Xf06A74SC405', {}).get('value', '')
            job = profile_data['profile']['fields'].get('Xf069VGMDFC7', {}).get('value', '')
            team = profile_data['profile']['fields'].get('Xf06AJGM49AP', {}).get('value', '')

            # ファイルに書き出し
            file.write(f"ID: {user_id}\n")
            file.write(f"名前: {real_name}\n")
            file.write(f"担当自治体: {local_gov}\n")
            file.write(f"ポルト: {port}\n")
            file.write(f"職種: {job}\n")
            file.write(f"所属チーム: {team}\n")
            file.write("\n")
