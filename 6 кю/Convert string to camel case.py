def to_camel_case(text):
    try:
        new = ''
        for i in text.replace('-',' ').replace('_', ' ').split():
            new += i.title()
        if text[0] == new[0]:
            return new
        else:
            return new.replace(f'{new[0]}',f'{new[0].lower()}')
    except IndexError:
        return ''
