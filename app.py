class Armor:
    def __init__(self, *args):
        self._attrs = dict()
        for item in args:
            if not isinstance(item, tuple):
                continue

            if len(item) < 2:
                continue

            k, v = item[0], item[1]

            if not isinstance(k, str):
                continue

            if not isinstance(v, int):
                v = 0

            self._attrs[k] = v

    def __repr__(self):
        return self._get_repr()

    def _has_attrs(self):
        return len(self._attrs) > 0

    def _default_repr(self):
        return self.__class__.__name__

    def _get_sorted_attrs(self):
        return [f'{_tuple[0]}: {_tuple[1]}' for _tuple in sorted(self._attrs.items())]

    def _get_attrs_repr(self):
        return ", ".join(self._get_sorted_attrs())

    def _get_repr(self):
        return f'{self._default_repr()}({self._get_attrs_repr()})'

    def add(self, key):
        if not isinstance(key, str):
            return

        if key in self._attrs:
            self._attrs[key] += 1
            return

        self._attrs[key] = 1


class GhostInArmor(Armor):
    _default_name = 'Canterville'

    def __init__(self, *args, name=None):
        super().__init__(self, *args)
        self._name = name if name else self._default_name

    def __repr__(self):
        return self._get_verbose_repr()

    def _get_verbose_repr(self):
        name_repr = f'name="{self._name}"'
        if not self._has_attrs():
            return f'{self._default_repr()}({name_repr}))'

        return f'{self._default_repr()}({self._get_attrs_repr()}, {name_repr})'

    def get(self, key):
        return self._attrs.get(key)

    def drop(self, key):
        self._attrs.pop(key, None)

    def items(self):
        return self._get_sorted_attrs()

    def len(self):
        return len(self._attrs)


if __name__ == '__main__':
    print("--- Armor ---")
    a = Armor(("helmet", 1), ("ring", 2), (1, 2), ("sword", None), ("only key",))
    print(a)
    a.add('helmet')
    a.add('arrow')
    print(a)

    print("--- GhostInArmor ---")
    gia = GhostInArmor(("helmet", 1), ("ring", 2), (1, 2), ("sword", None), ("only key",))
    print(gia)

    attr = 'horse'
    gia.add(attr)
    print(f'added {attr}')
    print(gia)

    unwanted_attrs = ("sword", "glasses", "icecream")
    for attr in unwanted_attrs:
        gia.drop(attr)

    print(f'dropped: {", ".join(unwanted_attrs)}')
    print(gia)

    attr = 'ring'
    print(f'qty of attr "ring": {gia.get(attr)}')

    print(f'sorted attrs: {gia.items()}')
