# Generated by Django 3.1 on 2020-08-15 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscribe', '0005_auto_20200813_0400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscribe',
            name='country',
            field=models.CharField(choices=[('afghanistan', 'Afghanistan'), ('albania', 'Albania'), ('algeria', 'Algeria'), ('andorra', 'Andorra'), ('angola', 'Angola'), ('antiguaandbarbuda', 'Antiguaandbarbuda'), ('argentina', 'Argentina'), ('armenia', 'Armenia'), ('australia', 'Australia'), ('austria', 'Austria'), ('austrianempire', 'Austrianempire'), ('azerbaijan', 'Azerbaijan'), ('baden', 'Baden'), ('bahamasthe', 'Bahamasthe'), ('bahrain', 'Bahrain'), ('bangladesh', 'Bangladesh'), ('barbados', 'Barbados'), ('bavaria', 'Bavaria'), ('belarus', 'Belarus'), ('belgium', 'Belgium'), ('belize', 'Belize'), ('benin', 'Benin'), ('bolivia', 'Bolivia'), ('bosniaandherzegovina', 'Bosniaandherzegovina'), ('botswana', 'Botswana'), ('brazil', 'Brazil'), ('brunei', 'Brunei'), ('brunswickandlneburg', 'Brunswickandlneburg'), ('bulgaria', 'Bulgaria'), ('burkinafaso', 'Burkinafaso'), ('burma', 'Burma'), ('burundi', 'Burundi'), ('caboverde', 'Caboverde'), ('cambodia', 'Cambodia'), ('cameroon', 'Cameroon'), ('canada', 'Canada'), ('caymanislandsthe', 'Caymanislandsthe'), ('centralafricanrepublic', 'Centralafricanrepublic'), ('centralamericanfederation', 'Centralamericanfederation'), ('chad', 'Chad'), ('chile', 'Chile'), ('china', 'China'), ('colombia', 'Colombia'), ('comoros', 'Comoros'), ('congofreestatethe', 'Congofreestatethe'), ('costarica', 'Costarica'), ('cotedivoire', 'Cotedivoire'), ('croatia', 'Croatia'), ('cuba', 'Cuba'), ('cyprus', 'Cyprus'), ('czechia', 'Czechia'), ('czechoslovakia', 'Czechoslovakia'), ('democraticrepublicofthecongo', 'Democraticrepublicofthecongo'), ('denmark', 'Denmark'), ('djibouti', 'Djibouti'), ('dominica', 'Dominica'), ('dominicanrepublic', 'Dominicanrepublic'), ('duchyofparmathe', 'Duchyofparmathe'), ('eastgermany', 'Eastgermany'), ('ecuador', 'Ecuador'), ('egypt', 'Egypt'), ('elsalvador', 'Elsalvador'), ('equatorialguinea', 'Equatorialguinea'), ('eritrea', 'Eritrea'), ('estonia', 'Estonia'), ('eswatini', 'Eswatini'), ('ethiopia', 'Ethiopia'), ('federalgovernmentofgermany', 'Federalgovernmentofgermany'), ('fiji', 'Fiji'), ('finland', 'Finland'), ('france', 'France'), ('gabon', 'Gabon'), ('gambiathe', 'Gambiathe'), ('georgia', 'Georgia'), ('germany', 'Germany'), ('ghana', 'Ghana'), ('grandduchyoftuscanythe', 'Grandduchyoftuscanythe'), ('greece', 'Greece'), ('grenada', 'Grenada'), ('guatemala', 'Guatemala'), ('guinea', 'Guinea'), ('guinea-bissau', 'Guinea-bissau'), ('guyana', 'Guyana'), ('haiti', 'Haiti'), ('hanover', 'Hanover'), ('hanseaticrepublics', 'Hanseaticrepublics'), ('hawaii', 'Hawaii'), ('hesse', 'Hesse'), ('holysee', 'Holysee'), ('honduras', 'Honduras'), ('hungary', 'Hungary'), ('iceland', 'Iceland'), ('india', 'India'), ('indonesia', 'Indonesia'), ('iran', 'Iran'), ('iraq', 'Iraq'), ('ireland', 'Ireland'), ('israel', 'Israel'), ('italy', 'Italy'), ('jamaica', 'Jamaica'), ('japan', 'Japan'), ('jordan', 'Jordan'), ('kazakhstan', 'Kazakhstan'), ('kenya', 'Kenya'), ('kingdomofserbiayugoslavia', 'Kingdomofserbiayugoslavia'), ('kiribati', 'Kiribati'), ('korea', 'Korea'), ('kosovo', 'Kosovo'), ('kuwait', 'Kuwait'), ('kyrgyzstan', 'Kyrgyzstan'), ('laos', 'Laos'), ('latvia', 'Latvia'), ('lebanon', 'Lebanon'), ('lesotho', 'Lesotho'), ('lewchew', 'Lewchew'), ('liberia', 'Liberia'), ('libya', 'Libya'), ('liechtenstein', 'Liechtenstein'), ('lithuania', 'Lithuania'), ('luxembourg', 'Luxembourg'), ('madagascar', 'Madagascar'), ('malawi', 'Malawi'), ('malaysia', 'Malaysia'), ('maldives', 'Maldives'), ('mali', 'Mali'), ('malta', 'Malta'), ('marshallislands', 'Marshallislands'), ('mauritania', 'Mauritania'), ('mauritius', 'Mauritius'), ('mecklenburg-schwerin', 'Mecklenburg-schwerin'), ('mecklenburg-strelitz', 'Mecklenburg-strelitz'), ('mexico', 'Mexico'), ('micronesia', 'Micronesia'), ('moldova', 'Moldova'), ('monaco', 'Monaco'), ('mongolia', 'Mongolia'), ('montenegro', 'Montenegro'), ('morocco', 'Morocco'), ('mozambique', 'Mozambique'), ('namibia', 'Namibia'), ('nassau', 'Nassau'), ('nauru', 'Nauru'), ('nepal', 'Nepal'), ('netherlandsthe', 'Netherlandsthe'), ('newzealand', 'Newzealand'), ('nicaragua', 'Nicaragua'), ('niger', 'Niger'), ('nigeria', 'Nigeria'), ('northgermanconfederation', 'Northgermanconfederation'), ('northgermanunion', 'Northgermanunion'), ('northmacedonia', 'Northmacedonia'), ('norway', 'Norway'), ('oldenburg', 'Oldenburg'), ('oman', 'Oman'), ('orangefreestate', 'Orangefreestate'), ('pakistan', 'Pakistan'), ('palau', 'Palau'), ('panama', 'Panama'), ('papalstates', 'Papalstates'), ('papuanewguinea', 'Papuanewguinea'), ('paraguay', 'Paraguay'), ('peru', 'Peru'), ('philippines', 'Philippines'), ('piedmont-sardinia', 'Piedmont-sardinia'), ('poland', 'Poland'), ('portugal', 'Portugal'), ('qatar', 'Qatar'), ('republicofgenoa', 'Republicofgenoa'), ('republicofkorea', 'Republicofkorea'), ('republicofthecongo', 'Republicofthecongo'), ('romania', 'Romania'), ('russia', 'Russia'), ('rwanda', 'Rwanda'), ('saintkittsandnevis', 'Saintkittsandnevis'), ('saintlucia', 'Saintlucia'), ('saintvincentandthegrenadines', 'Saintvincentandthegrenadines'), ('samoa', 'Samoa'), ('sanmarino', 'Sanmarino'), ('saotomeandprincipe', 'Saotomeandprincipe'), ('saudiarabia', 'Saudiarabia'), ('schaumburg-lippe', 'Schaumburg-lippe'), ('senegal', 'Senegal'), ('serbia', 'Serbia'), ('seychelles', 'Seychelles'), ('sierraleone', 'Sierraleone'), ('singapore', 'Singapore'), ('slovakia', 'Slovakia'), ('slovenia', 'Slovenia'), ('solomonislandsthe', 'Solomonislandsthe'), ('somalia', 'Somalia'), ('southafrica', 'Southafrica'), ('southsudan', 'Southsudan'), ('spain', 'Spain'), ('srilanka', 'Srilanka'), ('sudan', 'Sudan'), ('suriname', 'Suriname'), ('sweden', 'Sweden'), ('switzerland', 'Switzerland'), ('syria', 'Syria'), ('tajikistan', 'Tajikistan'), ('tanzania', 'Tanzania'), ('texas', 'Texas'), ('thailand', 'Thailand'), ('timor-leste', 'Timor-leste'), ('togo', 'Togo'), ('tonga', 'Tonga'), ('trinidadandtobago', 'Trinidadandtobago'), ('tunisia', 'Tunisia'), ('turkey', 'Turkey'), ('turkmenistan', 'Turkmenistan'), ('tuvalu', 'Tuvalu'), ('twosicilies', 'Twosicilies'), ('uganda', 'Uganda'), ('ukraine', 'Ukraine'), ('unionofsovietsocialistrepublics', 'Unionofsovietsocialistrepublics'), ('unitedarabemiratesthe', 'Unitedarabemiratesthe'), ('unitedkingdomthe', 'Unitedkingdomthe'), ('uruguay', 'Uruguay'), ('uzbekistan', 'Uzbekistan'), ('vanuatu', 'Vanuatu'), ('venezuela', 'Venezuela'), ('vietnam', 'Vietnam'), ('wrttemberg', 'Wrttemberg'), ('yemen', 'Yemen'), ('zambia', 'Zambia'), ('zimbabwe', 'Zimbabwe')], max_length=100, null=True),
        ),
    ]