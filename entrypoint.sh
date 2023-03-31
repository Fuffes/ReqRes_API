set -ex
pytest -s -v --alluredir=allure_results
allure serve allure_results