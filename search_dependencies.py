import requests


package_name = "streamlit"
version = '1.4.0'
url = f"https://pypi.org/pypi/{package_name}/{version}/json"
json = requests.get(url).json()

# このJSONはかなりでかい
print(len(str(json)))
# 113699

# JSONのkeys。 この中の　info が必要な情報を含んでいる。
print(json.keys())
# dict_keys(['info', 'last_serial', 'releases', 'urls', 'vulnerabilities'])

# infoの下に、多くの情報がある。
print(json["info"].keys())
"""
dict_keys(['author', 'author_email', 'bugtrack_url', 'classifiers',
        'description', 'description_content_type', 'docs_url', 'download_url',
        'downloads', 'home_page', 'keywords', 'license', 'maintainer',
        'maintainer_email', 'name', 'package_url', 'platform', 'project_url',
        'project_urls', 'release_url', 'requires_dist', 'requires_python',
        'summary', 'version', 'yanked', 'yanked_reason'])
"""

# requires_dist が依存ライブラリの情報。リスト形式なので、順番に表示する
for requires_dist_text in json["info"]["requires_dist"]:
    print(requires_dist_text)