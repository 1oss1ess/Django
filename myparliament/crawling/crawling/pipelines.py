# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import re
from parliament.models import ParliamentMembers


def cleane_name(param):
    return param


def cleane_date_birth(param):
    return re.findall(r'\d[0-9\-\/]*', param)[0]


def clean_place_birth(param):
    pattern = r'[а-яА-Я]+'
    param = param.split(':')
    return ' '.join(re.findall(pattern, param[1]))


def clean_languages(param):
    return param.split(':')[1].replace(';', ' ').strip()


def clean_email(param):
    return param


def clean_profession(param):
    return param.split(':')[1].replace(';', ' ').strip()


def clean_selected_with(param):
    pattern = r'[а-яА-Я]+'
    return ' '.join(re.findall(pattern, param.split(':')[1]))


def clean_image(param):
    if param == '':
        return param
    return 'https://www.parliament.bg' + param


class CrawlingPipeline:
    def process_item(self, item, spider):
        name = ''
        date_birth = ''
        place_birth = ''
        profession = ''
        languages = ''
        selected_with = ''
        email = ''
        image = ''
        for i in item:
            if i in 'name':
                name = cleane_name(item['name'])
            if i in 'place_birth':
                place_birth = clean_place_birth(item['place_birth'])
            if i in 'date_birth':
                date_birth = cleane_date_birth(item['date_birth'])
            if i in 'profession':
                profession = clean_profession(item['profession'])
            if i in 'languages':
                languages = clean_languages(item['languages'])
            if i in 'email':
                email = clean_email(item['email'])
            if i in 'selected_with':
                selected_with = clean_selected_with(item['selected_with'])
            if i in 'image':
                image = clean_image(item['image'])

        parlament = ParliamentMembers(
            name=name,
            date_birth=date_birth,
            place_birth=place_birth,
            profession=profession,
            languages=languages,
            selected_with=selected_with,
            email=email,
            image=image,
        )
        parlament.save()
        return item
