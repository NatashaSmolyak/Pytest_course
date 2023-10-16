class RegistrationSystem:
    def __init__(self):
        # Используем словарь для хранения данных пользователей
        # Ключом будет e-mail, значением - другой словарь с именем и номером телефона
        self.users = {}

    # Регистрация нового пользователя
    def register(self, name, email, phone):
        if email in self.users:
            return " Ошибка! Пользователь с таким email уже существует!"
        # Сохраняем пользователя в формате {"email", "name", "phone"}
        self.users[email] = {'name': name, 'phone': phone, "email": email}
        return "Пользователь успешно зарегистрирован!"

    # Удаление всех пользователей
    def delete_all_users(self):
        self.users = {}
        return "Все пользователи успешно удалены!"

    # Удаление пользователя по email
    def delete_user_by_email(self, email):
        if email not in self.users:
            return "Ошибка! Пользователь с таким email не найден!"
        del self.users[email]
        return f'Пользователь с email {email} успешно удален!'

    def view_all_users(self):
        return self.users

    # Пример использования
system = RegistrationSystem()

# Регистрация пользователя
print(system.register("Nata", "nata@example.com", "+1234567890"))
# Просмотр всех пользователей
print(system.view_all_users())
# Удаление пользователя по email
print(system.delete_user_by_email("nata@example.com"))
# Удаление всех пользователей
print(system.delete_all_users())