from rest_framework.schemas.openapi import AutoSchema


class ProductSchema(AutoSchema):
    def get_operation(self, path, method):
        op = super().get_operation(path, method)
        # if method == 'GET' and path == '/api/products/':
        #     op['parameters'].extend([
        #         {
        #             "name": "sortBy",
        #             "in": "query",
        #             "description": "Сортировка",
        #             'schema': {'type': 'string'}
        #         },
        #         {
        #             "name": "types_list",
        #             "in": "query",
        #             "description": "Вернуть только те товары, которые входят в указанные категории",
        #             'schema': {
        #                 'type': 'array',
        #                 'items': {'type': 'integer'}}
        #         },
        #         {
        #             "name": "favourite",
        #             "in": "query",
        #             "description": "Отобразить только товары с оценкой 4+",
        #             'schema': {'type': 'string'}
        #         }])
        return op
