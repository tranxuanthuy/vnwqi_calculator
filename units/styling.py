def generate_wqi_sld(output_path, attribute='wqi'):
    SLD = "http://www.opengis.net/sld"
    OGC = "http://www.opengis.net/ogc"
    XLINK = "http://www.w3.org/1999/xlink"
    XSI = "http://www.w3.org/2001/XMLSchema-instance"
    from lxml import etree    
    NSMAP = {
        None: SLD,
        'ogc': OGC,
        'xlink': XLINK,
        'xsi': XSI
    }

    color_rules = [
        (91, 999, '#3333ff', 'Rất tốt'),
        (76, 90,  '#00e400', 'Tốt'),
        (51, 75,  '#ffff00', 'Trung bình'),
        (26, 50,  '#ff7e00', 'Kém'),
        (10, 25,  '#ff0000', 'Rất kém'),
        (0, 9.99, '#7e2323', 'Ô nhiễm')
    ]

    sld = etree.Element("StyledLayerDescriptor", nsmap=NSMAP)
    sld.attrib["version"] = "1.0.0"
    sld.attrib[etree.QName(XSI, "schemaLocation")] = f"{SLD} StyledLayerDescriptor.xsd"

    named_layer = etree.SubElement(sld, "NamedLayer")
    etree.SubElement(named_layer, "Name").text = "WQI Layer"

    user_style = etree.SubElement(named_layer, "UserStyle")
    etree.SubElement(user_style, "Title").text = "WQI Classification"

    feature_type_style = etree.SubElement(user_style, "FeatureTypeStyle")

    for min_val, max_val, color, label in color_rules:
        rule = etree.SubElement(feature_type_style, "Rule")
        etree.SubElement(rule, "Title").text = label

        filter_tag = etree.SubElement(rule, etree.QName(OGC, "Filter"))
        and_tag = etree.SubElement(filter_tag, etree.QName(OGC, "And"))

        prop_gte = etree.SubElement(and_tag, etree.QName(OGC, "PropertyIsGreaterThanOrEqualTo"))
        etree.SubElement(prop_gte, etree.QName(OGC, "PropertyName")).text = attribute
        etree.SubElement(prop_gte, etree.QName(OGC, "Literal")).text = str(min_val)

        prop_lte = etree.SubElement(and_tag, etree.QName(OGC, "PropertyIsLessThanOrEqualTo"))
        etree.SubElement(prop_lte, etree.QName(OGC, "PropertyName")).text = attribute
        etree.SubElement(prop_lte, etree.QName(OGC, "Literal")).text = str(max_val)

        point_symb = etree.SubElement(rule, "PointSymbolizer")
        graphic = etree.SubElement(point_symb, "Graphic")
        mark = etree.SubElement(graphic, "Mark")
        etree.SubElement(mark, "WellKnownName").text = "circle"
        fill = etree.SubElement(mark, "Fill")
        css = etree.SubElement(fill, "CssParameter", name="fill")
        css.text = color

        size = etree.SubElement(graphic, "Size")
        size.text = "8"

    with open(output_path, "wb") as f:
        f.write(etree.tostring(sld, pretty_print=True, xml_declaration=True, encoding='UTF-8'))

    print(f"✅ Đã tạo file SLD: {output_path}")
