import xml.etree.cElementTree as ET
import lxml.etree
from xml.etree.ElementTree import Element, SubElement, ElementTree
from xml.dom.minidom import parseString


def edit_value(root):
    for name in root.iter("company_name"):
        if name.text == 'Apple':
            name.text = 'Motorola'
    for price in root.iter('price'):
        if float(price.text) > 150.00:
            price.text = str(150.00)
    for rating in root.iter('rating'):
        if float(rating.text) < 4.0:
            rating.text = str(0.00)
    return root


def edit_attributes(root):
    for price in root.iter('price'):
        price.attrib['currency'] = 'euro'
    for rating in root.iter('rating'):
        del rating.attrib['max_value']
    for amount_of_customers in root.iter('amount_of_customers'):
        amount_of_customers.set('currency', 'people')
    return root


def elements_add(root):
    phone = SubElement(root, 'phone')
    phone.set('id', 'result_' + str(16))
    model_name = SubElement(phone, 'model_name')
    model_name.text = 'Xiaomi Redmi Note 8 Pro 6/128'
    company_name = SubElement(phone, 'company_name')
    company_name.text = 'Xiaomi'
    price = SubElement(phone, 'price')
    price.set('currency', 'euro')
    price.text = str(300)
    rating = SubElement(phone, 'rating')
    rating.text = str(5)
    amount_of_customers = SubElement(phone, 'amount_of_customers')
    amount_of_customers.set('currency', 'people')
    amount_of_customers.text = '10,785'

    for phone in root.iter('phone'):
        country = SubElement(phone, 'country')
        country.set('format', 'iso-3166')
        name = SubElement(country, 'name')
        code = SubElement(country, 'code')
        if phone.find('company_name').text == 'Samsung':
            name.text = 'South Korea'
            code.text = 'KR'
        elif phone.find('company_name').text == 'Xiaomi':
            name.text = 'China'
            code.text = 'CN'
        else:
            name.text = 'USA'
            code.text = 'US'
    return root


def prettify(tree, filename):
    with open(filename, "wb") as f:
        tree.write(f)
    with open(filename, 'r') as file:
        xml_text = file.read()
        prettified_xml = parseString(xml_text).toprettyxml()
        file.close()
    with open(filename, 'w') as file:
        file.write(prettified_xml)
        file.close()


def html_building():
    dom = lxml.etree.parse('data/updated.xml')
    xslt = lxml.etree.parse('data/updated.xslt')
    transform = lxml.etree.XSLT(xslt)
    newdom = transform(dom)
    with open('data/updated.html', 'w') as file:
        file.write(str(newdom))
        file.close()


if __name__ == '__main__':
    tree = ET.ElementTree(file="data/amazon.xml")
    root = tree.getroot()
    root = edit_value(root)
    root = edit_attributes(root)
    root = elements_add(root)
    tree = ET.ElementTree(root)
    prettify(tree, 'data/updated.xml')
    html_building()
