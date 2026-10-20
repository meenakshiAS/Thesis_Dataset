def move(self, category_id, parent_id, after_id=None):
    """
    Move category in tree.

    :param category_id: ID of category to move
    :param parent_id: New parent of the category
    :param after_id: Category ID after what position it will be moved
    :return: Boolean
    """
    return bool(
        self.call(
            'catalog_category.move',
            [category_id, parent_id, after_id]
        )
    )
