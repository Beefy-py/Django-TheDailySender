# Generated by Django 3.1 on 2020-08-13 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscribe', '0004_auto_20200812_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscribe',
            name='country',
            field=models.CharField(choices=[('afghanistan', 'Afghanistan'), ('albania', 'Albania'), ('algeria', 'Algeria'), ('andorra', 'Andorra'), ('angola', 'Angola'), ('antigua and barbuda', 'Antigua and barbuda'), ('argentina', 'Argentina'), ('armenia', 'Armenia'), ('australia', 'Australia'), ('austria', 'Austria'), ('austrian empire', 'Austrian empire'), ('azerbaijan', 'Azerbaijan'), ('baden*', 'Baden*'), ('bahamas, the', 'Bahamas, the'), ('bahrain', 'Bahrain'), ('bangladesh', 'Bangladesh'), ('barbados', 'Barbados'), ('bavaria*', 'Bavaria*'), ('belarus', 'Belarus'), ('belgium', 'Belgium'), ('belize', 'Belize'), ('benin (dahomey)', 'Benin (dahomey)'), ('bolivia', 'Bolivia'), ('bosnia and herzegovina', 'Bosnia and herzegovina'), ('botswana', 'Botswana'), ('brazil', 'Brazil'), ('brunei', 'Brunei'), ('brunswick and lüneburg', 'Brunswick and lüneburg'), ('bulgaria', 'Bulgaria'), ('burkina faso (upper volta)', 'Burkina faso (upper volta)'), ('burma', 'Burma'), ('burundi', 'Burundi'), ('cabo verde', 'Cabo verde'), ('cambodia', 'Cambodia'), ('cameroon', 'Cameroon'), ('canada', 'Canada'), ('cayman islands, the', 'Cayman islands, the'), ('central african republic', 'Central african republic'), ('central american federation*', 'Central american federation*'), ('chad', 'Chad'), ('chile', 'Chile'), ('china', 'China'), ('colombia', 'Colombia'), ('comoros', 'Comoros'), ('congo free state, the', 'Congo free state, the'), ('costa rica', 'Costa rica'), ('cote d’ivoire (ivory coast)', 'Cote d’ivoire (ivory coast)'), ('croatia', 'Croatia'), ('cuba', 'Cuba'), ('cyprus', 'Cyprus'), ('czechia', 'Czechia'), ('czechoslovakia', 'Czechoslovakia'), ('democratic republic of the congo', 'Democratic republic of the congo'), ('denmark', 'Denmark'), ('djibouti', 'Djibouti'), ('dominica', 'Dominica'), ('dominican republic', 'Dominican republic'), ('duchy of parma, the*', 'Duchy of parma, the*'), ('east germany (german democratic republic)', 'East germany (german democratic republic)'), ('ecuador', 'Ecuador'), ('egypt', 'Egypt'), ('el salvador', 'El salvador'), ('equatorial guinea', 'Equatorial guinea'), ('eritrea', 'Eritrea'), ('estonia', 'Estonia'), ('eswatini', 'Eswatini'), ('ethiopia', 'Ethiopia'), ('federal government of germany (1848-49)*', 'Federal government of germany (1848-49)*'), ('fiji', 'Fiji'), ('finland', 'Finland'), ('france', 'France'), ('gabon', 'Gabon'), ('gambia, the', 'Gambia, the'), ('georgia', 'Georgia'), ('germany', 'Germany'), ('ghana', 'Ghana'), ('grand duchy of tuscany, the*', 'Grand duchy of tuscany, the*'), ('greece', 'Greece'), ('grenada', 'Grenada'), ('guatemala', 'Guatemala'), ('guinea', 'Guinea'), ('guinea-bissau', 'Guinea-bissau'), ('guyana', 'Guyana'), ('haiti', 'Haiti'), ('hanover*', 'Hanover*'), ('hanseatic republics*', 'Hanseatic republics*'), ('hawaii*', 'Hawaii*'), ('hesse*', 'Hesse*'), ('holy see', 'Holy see'), ('honduras', 'Honduras'), ('hungary', 'Hungary'), ('iceland', 'Iceland'), ('india', 'India'), ('indonesia', 'Indonesia'), ('iran', 'Iran'), ('iraq', 'Iraq'), ('ireland', 'Ireland'), ('israel', 'Israel'), ('italy', 'Italy'), ('jamaica', 'Jamaica'), ('japan', 'Japan'), ('jordan', 'Jordan'), ('kazakhstan', 'Kazakhstan'), ('kenya', 'Kenya'), ('kingdom of serbia/yugoslavia*', 'Kingdom of serbia/yugoslavia*'), ('kiribati', 'Kiribati'), ('korea', 'Korea'), ('kosovo', 'Kosovo'), ('kuwait', 'Kuwait'), ('kyrgyzstan', 'Kyrgyzstan'), ('laos', 'Laos'), ('latvia', 'Latvia'), ('lebanon', 'Lebanon'), ('lesotho', 'Lesotho'), ('lew chew (loochoo)*', 'Lew chew (loochoo)*'), ('liberia', 'Liberia'), ('libya', 'Libya'), ('liechtenstein', 'Liechtenstein'), ('lithuania', 'Lithuania'), ('luxembourg', 'Luxembourg'), ('madagascar', 'Madagascar'), ('malawi', 'Malawi'), ('malaysia', 'Malaysia'), ('maldives', 'Maldives'), ('mali', 'Mali'), ('malta', 'Malta'), ('marshall islands', 'Marshall islands'), ('mauritania', 'Mauritania'), ('mauritius', 'Mauritius'), ('mecklenburg-schwerin*', 'Mecklenburg-schwerin*'), ('mecklenburg-strelitz*', 'Mecklenburg-strelitz*'), ('mexico', 'Mexico'), ('micronesia', 'Micronesia'), ('moldova', 'Moldova'), ('monaco', 'Monaco'), ('mongolia', 'Mongolia'), ('montenegro', 'Montenegro'), ('morocco', 'Morocco'), ('mozambique', 'Mozambique'), ('namibia', 'Namibia'), ('nassau*', 'Nassau*'), ('nauru', 'Nauru'), ('nepal', 'Nepal'), ('netherlands, the', 'Netherlands, the'), ('new zealand', 'New zealand'), ('nicaragua', 'Nicaragua'), ('niger', 'Niger'), ('nigeria', 'Nigeria'), ('north german confederation*', 'North german confederation*'), ('north german union*', 'North german union*'), ('north macedonia', 'North macedonia'), ('norway', 'Norway'), ('oldenburg*', 'Oldenburg*'), ('oman', 'Oman'), ('orange free state*', 'Orange free state*'), ('pakistan', 'Pakistan'), ('palau', 'Palau'), ('panama', 'Panama'), ('papal states*', 'Papal states*'), ('papua new guinea', 'Papua new guinea'), ('paraguay', 'Paraguay'), ('peru', 'Peru'), ('philippines', 'Philippines'), ('piedmont-sardinia*', 'Piedmont-sardinia*'), ('poland', 'Poland'), ('portugal', 'Portugal'), ('qatar', 'Qatar'), ('republic of genoa*', 'Republic of genoa*'), ('republic of korea (south korea)', 'Republic of korea (south korea)'), ('republic of the congo', 'Republic of the congo'), ('romania', 'Romania'), ('russia', 'Russia'), ('rwanda', 'Rwanda'), ('saint kitts and nevis', 'Saint kitts and nevis'), ('saint lucia', 'Saint lucia'), ('saint vincent and the grenadines', 'Saint vincent and the grenadines'), ('samoa', 'Samoa'), ('san marino', 'San marino'), ('sao tome and principe', 'Sao tome and principe'), ('saudi arabia', 'Saudi arabia'), ('schaumburg-lippe*', 'Schaumburg-lippe*'), ('senegal', 'Senegal'), ('serbia', 'Serbia'), ('seychelles', 'Seychelles'), ('sierra leone', 'Sierra leone'), ('singapore', 'Singapore'), ('slovakia', 'Slovakia'), ('slovenia', 'Slovenia'), ('solomon islands, the', 'Solomon islands, the'), ('somalia', 'Somalia'), ('south africa', 'South africa'), ('south sudan', 'South sudan'), ('spain', 'Spain'), ('sri lanka', 'Sri lanka'), ('sudan', 'Sudan'), ('suriname', 'Suriname'), ('sweden', 'Sweden'), ('switzerland', 'Switzerland'), ('syria', 'Syria'), ('tajikistan', 'Tajikistan'), ('tanzania', 'Tanzania'), ('texas*', 'Texas*'), ('thailand', 'Thailand'), ('timor-leste', 'Timor-leste'), ('togo', 'Togo'), ('tonga', 'Tonga'), ('trinidad and tobago', 'Trinidad and tobago'), ('tunisia', 'Tunisia'), ('turkey', 'Turkey'), ('turkmenistan', 'Turkmenistan'), ('tuvalu', 'Tuvalu'), ('two sicilies*', 'Two sicilies*'), ('uganda', 'Uganda'), ('ukraine', 'Ukraine'), ('union of soviet socialist republics*', 'Union of soviet socialist republics*'), ('united arab emirates, the', 'United arab emirates, the'), ('united kingdom, the', 'United kingdom, the'), ('uruguay', 'Uruguay'), ('uzbekistan', 'Uzbekistan'), ('vanuatu', 'Vanuatu'), ('venezuela', 'Venezuela'), ('vietnam', 'Vietnam'), ('württemberg*', 'Württemberg*'), ('yemen', 'Yemen'), ('zambia', 'Zambia'), ('zimbabwe', 'Zimbabwe')], max_length=100, null=True),
        ),
    ]
