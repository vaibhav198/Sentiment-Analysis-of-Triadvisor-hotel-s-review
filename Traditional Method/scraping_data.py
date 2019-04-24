import requests
import os
from bs4 import BeautifulSoup
import pandas as pd


headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}


# list of urls of all the hotels whose reviews I am going to collect
urls = ['https://www.tripadvisor.in/Hotel_Review-g304551-d3507485-Reviews-Red_Fox_Hotel_Delhi_Airport-New_Delhi_National_Capital_Territory_of_Delhi.html',
'https://www.tripadvisor.in/Hotel_Review-g304555-d776155-Reviews-Hotel_Kalyan-Jaipur_Jaipur_District_Rajasthan.html',
'https://www.tripadvisor.in/Hotel_Review-g304551-d299120-Reviews-The_Lalit_New_Delhi-New_Delhi_National_Capital_Territory_of_Delhi.html',
'https://www.tripadvisor.in/Hotel_Review-g304551-d11561000-Reviews-Roseate_House_New_Delhi-New_Delhi_National_Capital_Territory_of_Delhi.html',
'https://www.tripadvisor.in/Hotel_Review-g8342248-d10390860-Reviews-Parakkat_Nature_Hotels_Resorts-Pallivasal_Munnar_Idukki_District_Kerala.html',
'https://www.tripadvisor.in/Hotel_Review-g304555-d304576-Reviews-Shahpura_House-Jaipur_Jaipur_District_Rajasthan.html',
'https://www.tripadvisor.in/Hotel_Review-g303890-d604848-Reviews-Villa_Retreat-Kodaikanal_Dindigul_District_Tamil_Nadu.html',
'https://www.tripadvisor.in/Hotel_Review-g297605-d651438-Reviews-Santana_Beach_Resort-Candolim_Bardez_North_Goa_District_Goa.html',
'https://www.tripadvisor.in/Hotel_Review-g297685-d609694-Reviews-Ganpati_Guest_House-Varanasi_Varanasi_District_Uttar_Pradesh.html',
'https://www.tripadvisor.in/Hotel_Review-g297685-d12961092-Reviews-Hotel_Varanasi_Inn-Varanasi_Varanasi_District_Uttar_Pradesh.html',
'https://www.tripadvisor.in/Hotel_Review-g297685-d1022189-Reviews-Hotel_Buddha-Varanasi_Varanasi_District_Uttar_Pradesh.html',
'https://www.tripadvisor.in/Hotel_Review-g297685-d11910987-Reviews-Dwivedi_Hotels_Sri_Omkar_Palace-Varanasi_Varanasi_District_Uttar_Pradesh.html',
'https://www.tripadvisor.in/Hotel_Review-g297683-d1930271-Reviews-Hotel_Taj_Resorts-Agra_Agra_District_Uttar_Pradesh.html',
'https://www.tripadvisor.in/Hotel_Review-g297683-d8701436-Reviews-Parador_A_Boutique_Hotel-Agra_Agra_District_Uttar_Pradesh.html',
'https://www.tripadvisor.in/Hotel_Review-g297683-d301771-Reviews-ITC_Mughal_Agra_a_Luxury_Collection_Hotel-Agra_Agra_District_Uttar_Pradesh.html',
'https://www.tripadvisor.in/Hotel_Review-g297683-d2248251-Reviews-Radisson_Blu_Agra_Taj_East_Gate-Agra_Agra_District_Uttar_Pradesh.html',
'https://www.tripadvisor.in/Hotel_Review-g635749-d6376843-Reviews-Bella_Vista_Resort-Mahabaleshwar_Satara_District_Maharashtra.html',
'https://www.tripadvisor.in/Hotel_Review-g304554-d299124-Reviews-The_Lalit_Mumbai-Mumbai_Maharashtra.html',
'https://www.tripadvisor.in/Hotel_Review-g304551-d306957-Reviews-Radisson_Blu_Plaza_Delhi_Airport-New_Delhi_National_Capital_Territory_of_Delhi.html',
'https://www.tripadvisor.in/Hotel_Review-g667810-d13799892-Reviews-Radisson_Gwalior-Gwalior_Gwalior_District_Madhya_Pradesh.html',
'https://www.tripadvisor.in/Hotel_Review-g667810-d2705115-Reviews-Neemrana_s_Deo_Bagh-Gwalior_Gwalior_District_Madhya_Pradesh.html',
'https://www.tripadvisor.in/Hotel_Review-g667810-d1789787-Reviews-Hotel_Grace-Gwalior_Gwalior_District_Madhya_Pradesh.html',
'https://www.tripadvisor.in/Hotel_Review-g667810-d658719-Reviews-Tansen_Residency-Gwalior_Gwalior_District_Madhya_Pradesh.html',
'https://www.tripadvisor.in/Hotel_Review-g667810-d634272-Reviews-Hotel_Gwalior_Regency-Gwalior_Gwalior_District_Madhya_Pradesh.html',
'https://www.tripadvisor.in/Hotel_Review-g297684-d305014-Reviews-Taj_Mahal_Lucknow-Lucknow_Lucknow_District_Uttar_Pradesh.html',
'https://www.tripadvisor.in/Hotel_Review-g297684-d13083452-Reviews-Radisson_Lucknow_City_Center-Lucknow_Lucknow_District_Uttar_Pradesh.html',
'https://www.tripadvisor.in/Hotel_Review-g297684-d302361-Reviews-La_Place_Sarovar_Portico_Lucknow-Lucknow_Lucknow_District_Uttar_Pradesh.html',
'https://www.tripadvisor.in/Hotel_Review-g297684-d12785074-Reviews-Fortune_Park_BBD-Lucknow_Lucknow_District_Uttar_Pradesh.html',
'https://www.tripadvisor.in/Hotel_Review-g297684-d10061337-Reviews-Lebua_Lucknow-Lucknow_Lucknow_District_Uttar_Pradesh.html',
'https://www.tripadvisor.in/Hotel_Review-g297628-d735365-Reviews-The_Monarch_Luxur-Bengaluru_Bangalore_District_Karnataka.html',
'https://www.tripadvisor.in/Hotel_Review-g297587-d3748122-Reviews-Fortune_Select_Grand_Ridge-Tirupati_Chittoor_District_Andhra_Pradesh.html',
'https://www.tripadvisor.in/Hotel_Review-g816969-d1220372-Reviews-Om_Sai_Beach_Huts-Agonda_South_Goa_District_Goa.html',
'https://www.tripadvisor.in/Hotel_Review-g297675-d10184114-Reviews-Hotel_Kiscol_Grands-Coimbatore_Coimbatore_District_Tamil_Nadu.html',
'https://www.tripadvisor.in/Hotel_Review-g303894-d13139721-Reviews-Hotel_Rameswaram_Grand-Rameswaram_Ramanathapuram_District_Tamil_Nadu.html',
'https://www.tripadvisor.in/Hotel_Review-g297628-d1400046-Reviews-Hotel_City_Centaur-Bengaluru_Bangalore_District_Karnataka.html',
'https://www.tripadvisor.in/Hotel_Review-g297628-d1400042-Reviews-Hill_View_Resorts-Bengaluru_Bangalore_District_Karnataka.html',
'https://www.tripadvisor.in/Hotel_Review-g297628-d1144028-Reviews-OYO_10885_Hotel_Keerthana_International-Bengaluru_Bangalore_District_Karnataka.html',
'https://www.tripadvisor.in/Hotel_Review-g297628-d3666489-Reviews-Royal_Inn_Hotel_Apartments-Bengaluru_Bangalore_District_Karnataka.html',
'https://www.tripadvisor.in/Hotel_Review-g297628-d1144202-Reviews-Roxel_Inn_Diamond_District-Bengaluru_Bangalore_District_Karnataka.html',
'https://www.tripadvisor.in/Hotel_Review-g297628-d4045459-Reviews-The_Woodbridge_Hotel_Delux_Lodging-Bengaluru_Bangalore_District_Karnataka.html'
]


# scraping the reviews from each element of the urls list
for url in urls:

	source_code = requests.get(url, headers=headers, timeout=15)
	plain_text = source_code.text
	soup = BeautifulSoup(plain_text,"html.parser")
	try:
		bubbles = [0,0,0,0,0]
		bubbles[0] = soup.findAll('span', {'class':'ui_bubble_rating bubble_10'})
		bubbles[1] = soup.findAll('span', {'class':'ui_bubble_rating bubble_20'})
		bubbles[2] = soup.findAll('span', {'class':'ui_bubble_rating bubble_30'})
		bubbles[3] = soup.findAll('span', {'class':'ui_bubble_rating bubble_40'})
		bubbles[4] = soup.findAll('span', {'class':'ui_bubble_rating bubble_50'})
		for i in range(0,5):
			for bubble in bubbles[i]:
				try:
					value = bubble.parent.next_sibling
					print(value.text)
					temp2 = [item.text for item in value]
					extra = [i+1]*len(temp2)
					
					# create a dataframe to store the reviews along with their status
					mapped = zip(temp2, extra)
					df = pd.DataFrame(list(mapped))
					with open('Dataset_.csv', 'a') as f:
						df.to_csv(f, header=False, index=False)
				except Exception as e:
					print(str(e))
	except Exception as e:
		print(str(e))

	print('Scrapped hotel review')
	

