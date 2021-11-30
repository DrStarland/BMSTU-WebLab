from rest_framework.schemas.openapi import *

class AutismSchema(AutoSchema):
    def get_responses(self, path, method):
        if method == 'DELETE':
            return {
                '204': {
                    'description': 'Запрос на удаление выполнен успешно.'
                },
                '401': {
                    'description': 'Пользователь не авторизован.'
                },
                '403': {
                    'description': 'Доступ запрещён.'
                },
                '404': {
                    'description': 'Страница не найдена.'
                }
            }

        self.response_media_types = self.map_renderers(path, method)

        serializer = self.get_serializer(path, method)

        if not isinstance(serializer, serializers.Serializer):
            item_schema = {}
        else:
            item_schema = self._get_reference(serializer)

        if is_list_view(path, method, self.view):
            response_schema = {
                'type': 'array',
                'items': item_schema,
            }
            paginator = self.get_paginator()
            if paginator:
                response_schema = paginator.get_paginated_response_schema(response_schema)
        else:
            response_schema = item_schema
        # method == 'POST' ? 201 : 200;
        if method == 'GET':
            return {
                '200': {
                    'content': {
                        ct: {'schema': response_schema}
                        for ct in self.response_media_types
                    },
                    'description': "Выполнено успешно."
                },
                '401': {
                    'description': 'Пользователь не авторизован.'
                },
                '404': {
                    'description': 'Страница не найдена.'
                }
            }
        elif method == 'POST':
            return {
                '201': {
                    'description': 'Выполнено успешно, ресурс создан.'
                },
                '400': {
                    'description': 'Сервер признал запрос невалидным.'
                },
                '401': {
                    'description': 'Пользователь не авторизован.'
                },
                '403': {
                    'description': 'Доступ запрещён.'
                },
                '404': {
                    'description': 'Страница не найдена.'
                },
                '405': {
                    'description': 'Данный метод не определён или не разрешён для данного объекта.'
                },
                '500': {
                    'description': 'Внутренняя ошибка на сервере.'
                }
            }
        elif method == 'PUT':
            return {
                '200': {
                    'description': 'Выполнено успешно, ресурс обновлён.'
                },
                '401': {
                    'description': 'Пользователь не авторизован.'
                },
                '403': {
                    'description': 'Доступ запрещён.'
                },
                '404': {
                    'description': 'Страница не найдена.'
                }
            }
        elif method == 'PATCH':
            return {
                '200': {
                    'description': 'Выполнено успешно, ресурс обновлён.'
                },
                '401': {
                    'description': 'Пользователь не авторизован.'
                },
                '403': {
                    'description': 'Доступ запрещён.'
                },
                '404': {
                    'description': 'Страница не найдена.'
                }
            }