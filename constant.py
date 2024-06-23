WEBNLG_RELATION_LIST_STRING = "[precededBy, legislature, areaTotal, designer, completionDate, floorArea, has to its north, leaderName, foundedBy, 3rd_runway_LengthFeet, OCLC_number, was a crew member of, fat, firstAppearanceInFilm, abbreviation, architect, placeOfBirth, outlookRanking, year, nickname, affiliations, 1st_runway_Number, mainIngredients, birthName, floorCount, order, distributor, owningOrganisation, CODEN_code, has to its northeast, largestCity, state, governingBody, height, hubAirport, address, part, compete in, publisher, river, 2nd_runway_SurfaceType, awards, municipality, district, ground, currentTenants, significantBuilding, jurisdiction, ICAO_Location_Identifier, course, languages, transportAircraft, populationTotal, senators, battles, operatingOrganisation, director, genus, postalCode, motto, officialSchoolColour, religion, was selected by NASA, season, leader, firstPublicationYear, administrativeCounty, mediaType, birthPlace, gemstone, sportsGoverningBody, architecturalStyle, LibraryofCongressClassification, demonym, class, locationCity, ISSN_number, title, aircraftFighter, chancellor, latinName, keyPerson, numberOfMembers, 1st_runway_LengthMetre, tenant, notableWork, category, representative, isPartOf, spokenIn, league, backup pilot, region, buildingStartDate, servingTemperature, commander, was given the 'Technical Campus' status by, ethnicGroup, runwayLength, developer, architecture, added to the National Register of Historic Places, fossil, family, child, academicStaffSize, owner, operator, residence, runwayName, inaugurationDate, nearestCity, elevationAboveTheSeaLevel_(in_metres), fullName, city, youthclub, has to its southwest, starring, followedBy, served as Chief of the Astronaut Office in, chairman, ReferenceNumber in the National Register of Historic Places, populationDensity, almaMater, dedicatedTo, IATA_Location_Identifier, officialLanguage, bird, editor, areaCode, chairperson, series, fullname, country, ingredient, voice, author, parentCompany, has to its northwest, founder, nativeName, numberOfUndergraduateStudents, regionServed, protein, president, areaOfWater, 3rd_runway_SurfaceType, alternativeName, location, anthem, campus, 1st_runway_SurfaceType, numberOfPages, creator, affiliation, ISBN_number, attackAircraft, club, 5th_runway_Number, award, established, 4th_runway_LengthFeet, genre, chief, elevationAboveTheSeaLevel_(in_feet), higher, creatorOfDish, capital, aircraftHelicopter, rector, placeOfDeath, EISSN_number, numberOfRooms, elevationAboveTheSeaLevel, areaOfLand, headquarter, numberOfStudents, nationality, product, countySeat, dishVariation, numberOfPostgraduateStudents, leaderParty, mayor, patronSaint, academicDiscipline, hometown, deathPlace, LCCN_number, language, significantProject, dean, currency, doctoralAdvisor, cityServed, material, 1st_runway_LengthFeet, sportsOffered, crewMembers, governmentType, bedCount, headquarters, has to its southeast, administrativeArrondissement, occupation, has to its west, yearOfConstruction, broadcastedBy, influencedBy, leaderTitle, champions, ethnicGroups, neighboringMunicipality, foundationPlace, manager, chairmanTitle]"
WEBNLG_EXAMPLE = '''
In: The 1st runway at Alderney Airport is made from Poaceae which is member of the Poales order.Poaceae belongs to the Commelinid order , within the flowering plants and classed as Monocotyledon .
Out: [(Alderney Airport, 1st_runway_SurfaceType, Poaceae),(Poaceae, order, Poales),(Poaceae, class, Monocotyledon)]
'''

WEBNLG_EXAMPLE_5 = '''
In: Alan B. Miller Hall in Williamsburg , Virginia was designed by Robert A.M. Stern and completed on June 1 , 2009 . It 's owner is the College of William and Mary .
Out: [(Alan B. Miller Hall, owner, College of William),(Alan B. Miller Hall, location, Williamsburg , Virginia),(Alan B. Miller Hall, architect, Robert)]
In: Alpena , Michigan is served by Alpena County Regional Airport which is located in Maple Ridge Township , Alpena County , Michigan at 210 metres above sea level and with a runway length of 2744.0 .
Out: [(Alpena County Regional Airport, location, Maple Ridge Township , Alpena County , Michigan),(Alpena County Regional Airport, runwayLength, 2744.0),(Alpena County Regional Airport, cityServed, Alpena , Michigan),(Alpena County Regional Airport, elevationAboveTheSeaLevel_(in_metres), 210)]
In: Arròs negre comes from the region of the Valencian Community ( leader Ximo Puig ) , Spain ( leader Felipe VI ) . Spaniards are the population name there .
Out: [(Arròs negre, region, Valencian Community),(Valencian Community, leaderName, Ximo Puig),(Arròs negre, country, Spain),(Spain, ethnicGroup, Spaniards),(Spain, leaderName, Felipe VI)]
In: Manhattan is part of New York City , which was part of New Netherland , and is the location of Asser Levy Public Baths .
Out: [(Asser Levy Public Baths, location, New York City),(New York City, isPartOf, Manhattan),(New York City, isPartOf, New Netherland)]
In: The manager of A.F.C . Blackpool is Stuart Parker who plays for Runcorn F.C . Halton and is attached to Irlam Town Football Club .
Out: [(A.F.C . Blackpool, manager, Stuart Parker),(Stuart Parker, club, Irlam Town),(Stuart Parker, club, Runcorn F.C . Halton)]
'''

# ---

WEBNLG_STAR_RELATION_LIST_STRING = "[1st_runway_LengthFeet, 1st_runway_LengthMetre, 1st_runway_Number, 1st_runway_SurfaceType, 3rd_runway_LengthFeet, 4th_runway_LengthFeet, 5th_runway_Number, EISSN_number, LCCN_number, OCLC_number, academicDiscipline, academicStaffSize, administrativeArrondissement, administrativeCounty, affiliation, affiliations, aircraftFighter, aircraftHelicopter, almaMater, anthem, architect, architecturalStyle, areaCode, attackAircraft, author, award, awards, backup pilot, battles, bedCount, bird, birthPlace, broadcastedBy, buildingStartDate, buildingType, capital, category, chairman, champions, chancellor, chief, child, city, cityServed, class, club, commander, compete in, completionDate, country, countySeat, creator, creatorOfDish, crewMembers, currency, currentTenants, dean, deathPlace, dedicatedTo, demonym, developer, dishVariation, district, division, doctoralAdvisor, editor, elevationAboveTheSeaLevel, elevationAboveTheSeaLevel_(in_feet), elevationAboveTheSeaLevel_(in_metres), established, ethnicGroup, ethnicGroups, family, firstPublicationYear, floorCount, followedBy, fossil, foundationPlace, foundedBy, founder, gemstone, genre, genus, governingBody, governmentType, ground, has to its north, has to its northeast, has to its northwest, has to its southeast, has to its southwest, has to its west, headquarter, headquarters, hometown, hubAirport, influencedBy, ingredient, isPartOf, jurisdiction, keyPerson, language, languages, largestCity, leader, leaderName, leaderParty, leaderTitle, league, literaryGenre, location, locationCity, mainIngredients, manager, mayor, mediaType, municipality, nationality, nearestCity, neighboringMunicipality, nickname, notableWork, numberOfMembers, numberOfPostgraduateStudents, numberOfRooms, numberOfStudents, numberOfUndergraduateStudents, occupation, officialLanguage, operatingOrganisation, operator, order, outlookRanking, owner, owningOrganisation, parentCompany, part, partsType, patronSaint, placeOfBirth, populationTotal, postalCode, precededBy, president, publisher, region, regionServed, religion, representative, residence, river, runwayLength, season, senators, served as Chief of the Astronaut Office in, significantBuilding, significantProject, spokenIn, sportsGoverningBody, sportsOffered, starring, state, tenant, title, transportAircraft, voice, was a crew member of, was given the 'Technical Campus' status by, was selected by NASA, year, yearOfConstruction]"
WEBNLG_STAR_EXAMPLE_5 = '''
In: The Mason School of Business are the current tenants of Alan B Miller Hall which is located in the United States . The architect of the Hall is Robert A M Stern and the building was completed on 1st June 2009 .
Out: [(Hall, architect, Stern),(Business, country, States),(Hall, currentTenants, Business)]
In: Standard Chinese is a language spoken in Singapore .
Out: [(Singapore, language, Chinese)]
In: Monroe Township is in Madison County which is a part of Indiana .
Out: [(Indiana, isPartOf, Indiana)]
In: James Pain and George Richard Pain are the architects of Adare Manor , which was completed in 1862 , and is owned by JP McManus .
Out: [(Manor, completionDate, 1862),(Manor, owner, McManus)]
In: Bandeja paisa is part of Columbian cuisine from the Antioquia Department area . It includes Avocado which is a plant of the laurales order , belonging to the Lauraceae family .
Out: [(paisa, ingredient, Avocado),(paisa, country, cuisine),(Avocado, family, Lauraceae),(paisa, region, Department)]
'''

# ---

NYT_RELATION_LIST_STRING = "[/business/company/advisors, /business/company/founders, /business/company/industry, /business/company/major_shareholders, /business/company/place_founded, /business/company_shareholder/major_shareholder_of, /business/person/company, /location/administrative_division/country, /location/country/administrative_divisions, /location/country/capital, /location/location/contains, /location/neighborhood/neighborhood_of, /people/deceased_person/place_of_death, /people/ethnicity/geographic_distribution, /people/ethnicity/people, /people/person/children, /people/person/ethnicity, /people/person/nationality, /people/person/place_lived, /people/person/place_of_birth, /people/person/profession, /people/person/religion, /sports/sports_team/location, /sports/sports_team_location/teams]"
NYT_EXAMPLE_5 = '''
In: The United States and Israel reacted skeptically , with President Bush urging tartly that Mr. Annan telephone President Bashar al-Assad of Syria , a key sponsor of Hezbollah , '' and make something happen . ''
Out: [(Bashar al-Assad, /people/person/nationality, Syria)]
In: Swan Lake '' : March 29 at 8 p.m. , at the State Theater , 15 Livingston Avenue , New Brunswick , N.J. , (732) 246-7469 -LRB- $ 20 , $ 30 and $ 35 -RRB- ; April 15 at 8 p.m. , at the Queensborough Performing Arts Center , Queensborough Community College , 222-05 56th Avenue , Bayside , Queens , (718) 631-6311 -LRB- $ 39 and $ 42 -RRB- .
Out: [(Queens, /location/location/contains, Bayside),(Queens, /location/location/contains, Queensborough Community College),(Bayside, /location/neighborhood/neighborhood_of, Queens)]
In: Driven by sectarian zeal , the Saudi authorities have razed and dug up virtually every site in Mecca and Medina linked to Muhammad , members of his family and his companions .
Out: [(Muhammad, /people/deceased_person/place_of_death, Medina)]
In: She has work in '' Edge of Desire '' and at Sepia International in Chelsea , plus a solo exhibition , '' Chairs , '' at the Isabella Stewart Gardner Museum in Boston , a really beautiful one , subtly globalist and time traveling .
Out: [(Boston, /location/location/contains, Isabella Stewart Gardner Museum)]
In: Do n't take this blip as significant , '' Ali al-Naimi , Saudi Arabia 's oil minister , told reporters in Vienna . ''
Out: [(Ali al-Naimi, /business/person/company, Saudi Arabia),(Ali al-Naimi, /people/person/nationality, Saudi Arabia)]
'''

# ---

NYT_STAR_RELATION_LIST_STRING = "[/business/company/advisors, /business/company/founders, /business/company/industry, /business/company/major_shareholders, /business/company/place_founded, /business/company_shareholder/major_shareholder_of, /business/person/company, /location/administrative_division/country, /location/country/administrative_divisions, /location/country/capital, /location/location/contains, /location/neighborhood/neighborhood_of, /people/deceased_person/place_of_death, /people/ethnicity/geographic_distribution, /people/ethnicity/people, /people/person/children, /people/person/ethnicity, /people/person/nationality, /people/person/place_lived, /people/person/place_of_birth, /people/person/profession, /people/person/religion, /sports/sports_team/location, /sports/sports_team_location/teams]"
NYT_STAR_EXAMPLE_5 = '''
In: The sport 's lore includes a quotation from Jacques Anquetil , who won the Tour five times , and once said , '' Only a fool would imagine it was possible to win the Tour de France on mineral water . ''
Out: [(Anquetil, /people/person/nationality, France)]
In: Automakers from the United States , Japan and Europe -- including Ford , General Motors , Toyota , DaimlerChrysler , Mazda and BMW -- are among the companies behind the campaign .
Out: [(Japan, /location/location/contains, Toyota)]
In: Mr. Fava 's draft report asserted that at least 1,245 C.I.A.-operated flights passed through Europe 's airspace or stopped at its airports , and listed Poland as among the countries least cooperative with its inquiry .
Out: [(Europe, /location/location/contains, Poland)]
In: He graduated from Worcester Polytechnic Institute and was in the Peace Corps from 1991 to 1993 , serving as an assistant livestock officer and agricultural adviser for Portland Parish in Port Antonio , Jamaica .
Out: [(Jamaica, /location/country/administrative_divisions, Parish),(Jamaica, /location/location/contains, Parish),(Parish, /location/administrative_division/country, Jamaica),(Jamaica, /location/location/contains, Antonio),(Parish, /location/location/contains, Antonio)]
In: Bear hunting is permissible in several other New England and mid-Atlantic states , including Maine and New York .
Out: [(England, /location/location/contains, Maine)]
'''

#---

NYT_HRL_RELATION_LIST_STRING = "[/location/administrative_division/country, /location/country/capital, /location/country/administrative_divisions, /location/neighborhood/neighborhood_of, /location/location/contains, /people/person/nationality, /people/person/place_lived, /people/deceased_person/place_of_death, /business/person/company, /location/us_state/capital, /people/person/place_of_birth, /people/person/children, /business/company/founders, /business/company/place_founded, /sports/sports_team/location, /people/person/ethnicity, /people/ethnicity/geographic_distribution, /people/person/religion, /business/company/major_shareholders, /location/province/capital, /location/br_state/capital, /business/company/advisors, /film/film_location/featured_in_films, /film/film/featured_film_locations, /location/us_county/county_seat, /time/event/locations, /people/deceased_person/place_of_burial, /people/place_of_interment/interred_here, /business/company_advisor/companies_advised]"
NYT_HRL_EXAMPLE_5 = '''
In: reebok , whose sale was completed on jan. 31 , will introduce a major branding campaign in september that will feature peyton manning , quarterback of the indianapolis colts ; vince young , quarterback of the tennessee titans and the hero of the last rose bowl ; steve smith , a wide receiver for the carolina panthers ; torry halt , a wide receiver for the st. louis rams ; deangelo hall , a defensive back for the atlanta falcons ; and roy williams , defensive back for the dallas cowboys .
Out: [(deangelo hall, /people/person/place_lived, atlanta)]
In: buffalo has very poor self-esteem , '' said marti gorman , one of the organizers , who lived in bogotá , colombia , as well as in atlanta and boulder , colo. , before she moved back to buffalo last november after her daughter enrolled at canisius college here . ''
Out: [(bogotá, /location/administrative_division/country, colombia),(colombia, /location/country/capital, bogotá),(colombia, /location/country/administrative_divisions, bogotá)]
In: the company , dubai ports world , which is controlled by the emir of dubai , part of the united arab emirates , asked the government to conduct '' the full 45-day investigation authorized under u.s. law , '' an investigation that mr. bush and his advisers said last week was unnecessary .
Out: [(united arab emirates, /location/country/administrative_divisions, dubai),(dubai, /location/administrative_division/country, united arab emirates)]
In: miami and miami-dade county officials said they were not moving forward haphazardly , but cataloging which shade trees survived the storms and which succumbed .
Out: [(miami-dade county, /location/location/contains, miami)]
In: on christmas eve of that year , a man known as old fish died of pneumonia at cumberland hospital in fort greene , brooklyn .
Out: [(fort greene, /location/neighborhood/neighborhood_of, brooklyn)]
'''