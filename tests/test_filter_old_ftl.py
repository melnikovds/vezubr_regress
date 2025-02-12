from pages.filter_old_ftl_page import OldFTL

# Инициализация класса
old_ftl = OldFTL(driver=None)

# URL API и функция логина
api_base_url = "https://api.example.com"
def api_login(role):
    # Здесь должна быть логика получения токена
    return "your-auth-token"

# Вызов метода для создания FTL
response = old_ftl.add_old_ftl_lkz(api_base_url, api_login)
print("Response:", response)