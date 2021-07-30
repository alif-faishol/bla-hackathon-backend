from database import session
from werkzeug.security import generate_password_hash, check_password_hash
from models import User, Usaha, Ulasan, ProposalModal, Order, Product

def initDB():
    users = (
        User(name='Arief',
             email='aryusniardi15@gmail.com',
             password=generate_password_hash('arief123'),
             phone='+6289656053383'),
        User(name='Alif',
             email='alifaishol@gmail.com',
             password=generate_password_hash('alif123'))
    )
    session.add_all(users)
    session.flush()

    usahas = (
        Usaha(name='Kerupuk Cap Sapi',
              user_id=users[0].id,
              alamat='Bandung Selatan',
              description='Kerupuk Sapi Enak'),
        Usaha(name='Baso Cap Sapi',
              user_id=users[0].id,
              alamat='Bandung Utara',
              description='Baso Enak')
    )
    session.add_all(usahas)
    session.flush()

    products = (
        Product(name='Kerupuk Kulit Sapi',
                description='Kerupuk dari kulit sapi',
                daily_production=12,
                price='20000',
                usaha_id=usahas[0].id),
        Product(name='Baso Kikil',
                description='Baso dengan extra kikil sapi',
                daily_production=3,
                price='25000',
                usaha_id=usahas[1].id)
    )
    session.add_all(products)

    proposals = (
        ProposalModal(title='Dana Pengembangan Kerupuk Kulit',
                      user_id=users[0].id,
                      content='Kami memerlukan dana untuk pengembangan usaha kerupuk kulit sapi kami.'),
        ProposalModal(title='Dana Pengembangan Cilok Cap Sapi',
                      user_id=users[0].id,
                      content='Kami memerlukan dana untuk pengembangan usaha cilok kami.')
    )
    session.add_all(proposals)

#    categories = (
#        Category(name='Fortune 1000'),
#        Category(name='New York Stock Exchange'),
#        Category(name='NASDAQ'),
#        Category(name='Trade Associations')
#    )
#    session.add_all(categories)
#
#    industries = (
#        Industry(name='Manufacturing'),
#        Industry(name='Retail Trade'),
#        Industry(name='Finance & Insurance'),
#        Industry(name='Natural Resources')
#    )
#    session.add_all(industries)
#    session.flush()
#
#    sectors = (
#        Sector(name='Oil Drilling & Gas Extraction', industry_id=industries[3].id),
#        Sector(name='Oil & Gas Machinery Manufacturing', industry_id=industries[0].id)
#    )
#    session.add_all(sectors)
#    session.flush()
#
#    companies = (
#        Company(name='Exxon Mobil',
#                sector_id=sectors[0].id,
#                category_id=categories[0].id,
#                nation='USA',
#                product='Crude Oil & Natural Gas',
#                description='Exxon Mobil Corporation, incorporated on August 5, 1882, is engaged in energy business. The company is engaged in the exploration, production, transportation and sale of crude oil and natural gas, and the manufacture.'),
#        Company(name='Chevron',
#                sector_id=sectors[0].id,
#                category_id=categories[0].id,
#                nation='USA',
#                product='Crude Oil & Natural Gas',
#                description='Chevron Corporation is an American multinational energy corporation. One of the successor companies of Standard Oil, is it headquartered in San Ramon, California, and active in more than 180 countries. Chevron is engaged in every aspect'),
#        Company(name='Caterpillar',
#                sector_id=sectors[1].id,
#                category_id=categories[0].id,
#                nation='USA',
#                product='Land Drilling Production, Well Service',
#                description='Caterpillar is a fortune 1000 company.'),
#        Company(name='Freeport Indonesia',
#                sector_id=sectors[0].id,
#                category_id=categories[0].id,
#                nation='Indonesia',
#                product='Gold',
#                description='Freeport Indonesia is a fortune 1000 company.'),
#        Company(name='Desert Oil',
#                sector_id=sectors[0].id,
#                category_id=categories[0].id,
#                nation='UAE',
#                product='Crude Oil & Natural Gas',
#                description='Desert Oil is a fortune 1000 company.')
#    )
#    session.add_all(companies)
#    session.flush()
#
#    companies[0].export_list.append(companies[3])
#    companies[0].export_list.append(companies[1])
#    companies[0].import_list.append(companies[2])
#    companies[1].export_list.append(companies[3])
#    companies[1].export_list.append(companies[4])
#    companies[1].import_list.append(companies[2])
#
#    companies[0].distribution_channels.append(companies[3])
#    companies[0].distribution_channels.append(companies[1])
#    companies[0].direct_suppliers.append(companies[2])
#    companies[1].distribution_channels.append(companies[3])
#    companies[1].distribution_channels.append(companies[4])
#    companies[1].direct_suppliers.append(companies[2])
#
    session.commit()
