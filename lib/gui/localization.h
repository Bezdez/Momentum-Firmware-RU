#ifndef LOCALIZATION_H
#define LOCALIZATION_H

#define LANG_RU 1
#define LANG_EN 0

#define LANGUAGE LANG_RU

#if LANGUAGE == LANG_RU
    #define TEXT_SETTINGS "Настройки"
    #define TEXT_MENU "Меню"
    #define TEXT_SAVE "Сохранить"
    #define TEXT_CANCEL "Отмена"
    #define TEXT_OK "ОК"
    #define TEXT_ERROR "Ошибка"
    #define TEXT_SUCCESS "Успешно"
    #define TEXT_LOAD "Загрузить"
    #define TEXT_EXIT "Выход"
#else
    #define TEXT_SETTINGS "TEXT_SETTINGS"
    #define TEXT_MENU "TEXT_MENU"
    #define TEXT_SAVE "TEXT_SAVE"
    #define TEXT_CANCEL "TEXT_CANCEL"
    #define TEXT_OK "TEXT_OK"
    #define TEXT_ERROR "TEXT_ERROR"
    #define TEXT_SUCCESS "TEXT_SUCCESS"
    #define TEXT_LOAD "TEXT_LOAD"
    #define TEXT_EXIT "TEXT_EXIT"
#endif

#endif // LOCALIZATION_H
