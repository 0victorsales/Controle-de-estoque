from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

#  ID da planilha
SAMPLE_SPREADSHEET_ID = '1-QaSFZJ8UfxIAQhckMGE9iLZOratARi1p71NbMcNYO8'
SAMPLE_RANGE_NAME = 'Página1!A1:B5'


def main():
    #Fazendo login para liberar acesso
    creds = None
    
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    
    
        
# Função para gravar valor na celula do item laranja
def Orange(add_laranja):
    update_laranja = add_laranja.get()
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    service = build('sheets', 'v4', credentials=creds)

    # Lista para atualizar valor da celula
    laranja = [
        [update_laranja],
    ]

    body = {'values': laranja}
    try:
            # Gravando valor na celula da laranja 
            result = service.spreadsheets().values().update(
                spreadsheetId= SAMPLE_SPREADSHEET_ID, range= "B2",
                valueInputOption="USER_ENTERED", body = body).execute()
            
            return result
    
    except HttpError as err:
            print(err)


def Sub_orange(sub_laranja):
    subtrair_laranja = 0
    subtrair_laranja = sub_laranja.get()
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    service = build('sheets', 'v4', credentials=creds)

    
    try:
            # Gravando valor na celula da laranja 
            result = service.spreadsheets().values().get(spreadsheetId= SAMPLE_SPREADSHEET_ID, range="B2").execute()
            a = result.get('values', [])
            subtracao = a - subtrair_laranja
            return subtracao
    
    except HttpError as err:
            print(err)


# Função para gravar valor na celula do item Pêra
def Pear(add_pera):
     update_pera = add_pera.get()
     creds = Credentials.from_authorized_user_file('token.json', SCOPES)
     service = build('sheets', 'v4', credentials=creds)
     
     # Lista para atualizar valor da celula
     pera = [
          [update_pera],
     ]

     body = {'values': pera}    
    
     try:
            # Gravando valor na celula da pêra 
            result = service.spreadsheets().values().update(
                spreadsheetId= SAMPLE_SPREADSHEET_ID, range= "B3",
                valueInputOption="USER_ENTERED", body = body).execute()
            
            return result
    
     except HttpError as err:
            print(err)




# Função para gravar valor na celula do item Uva
def Grape(add_uva):
     update_uva = add_uva.get()
     creds = Credentials.from_authorized_user_file('token.json', SCOPES)
     service = build('sheets', 'v4', credentials=creds)

     # Lista para atualizar valor da celula
     uva = [
          [update_uva],
     ]

     body = {'values': uva}

     try:
            # Gravando valor na celula da uva 
            result = service.spreadsheets().values().update(
                spreadsheetId= SAMPLE_SPREADSHEET_ID, range= "B4",
                valueInputOption="USER_ENTERED", body = body).execute()
            
            return result
    
     except HttpError as err:
            print(err)


# Função para gravar valor na celula do item Goiaba
def Guava(add_goiaba):
     update_goiaba = add_goiaba.get()
     creds = Credentials.from_authorized_user_file('token.json', SCOPES)
     service = build('sheets', 'v4', credentials=creds)

     # Lista para atualizar valor da celula
     goiaba = [
          [update_goiaba],
     ]

     body = {'values': goiaba}

     try:
            # Gravando valor na celula da goiaba 
            result = service.spreadsheets().values().update(
                spreadsheetId= SAMPLE_SPREADSHEET_ID, range= "B5",
                valueInputOption="USER_ENTERED", body = body).execute()
            
            return result
    
     except HttpError as err:
            print(err)



if __name__ == '__main__':
    main()

