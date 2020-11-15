import requests_html, requests, telebot, re, json
import random
import string
import string
from random import *
from time import sleep

bot = telebot.TeleBot("1338423319:AAFJUUdfIe-vXCleux6v1Yl1BL8NQZTR0BE")

PRIVADO = [640672725, 1057504279, 1248658385]
#
#
GRUPO = [-1001246683064, -1001180046189, -1001286277283, -1001252377898]


@bot.message_handler(commands=['start'])
def boavinda(message1):
    ide = message1.chat.id
    liste = PRIVADO
    if ide in liste:

        bot.send_message(ide, '<b>' '😎 OBA, VOCÊ TEM ACESSO! 😎' '</b>', parse_mode='HTML')
        bot.send_message(ide, '✅ ' '<b>' 'use ' '</b>''<code>' '/menu' '</code>''<b>' ' e veja os comandos' '</b>' ' ✅', parse_mode='HTML')
    
    else:
        bot.reply_to(message1, '<b>' + '🚫 ' + '@'+message1.chat.username + ' VOCÊ NÃO TEM ACESSO! 🚫' '</b>', parse_mode='HTML')
        bot.send_message(ide, '<b>' '✅ Adquira acesso com meus pais @Resenha1 e @Anonylions ✅' '</b>', parse_mode='HTML')
        
@bot.message_handler(commands=['cpf'])
def zn(nome):
            id1 = nome.chat.id

            ltnome = PRIVADO + GRUPO
            if id1 in ltnome:
                try:
                    msg = nome.text
                    fl = msg.split('/cpf')
                    ip = re.sub('[^0-9]', '', msg)
                    url = requests.get('https://cadsusnonny.000webhostapp.com/public_html/cpfsusDKZ.php?token=I2jlu2k2&cpf=' + ip)
                    req = url.json
                    op = req()['data_nasc'][6:10]
                    jog = 2020 - int(op)
                    reeq = url.json()
                    hels = bot.reply_to(nome, '<b>' '🔍 ☂️CONSULTA VIP REALIZADA ☂️🔎' '</b>' + '\n\n' + '<b>' '• CPF: ' '</b>' '<code>' + req()['cpf'] + '</code>' '\n' + '<b>' '• CNS: ' '</b>' '<code>' + req()['cns'] + '</code>' '\n' + '<b>' '• NOME: ' '</b>' '<code>' + req()['nome'] + '</code>' '\n' + '<b>' '• NASCIMENTO: ' '</b>' '<code>' + req()['data_nasc'] + '</code>' '\n' + '<b>' '• IDADE: ' '</b>' '<code>' + str(jog) + '</code>' + '\n' + '<b>' '• MÃE: ' '</b>' '<code>' + req()['nomeMae'] + '</code>' '\n' + '<b>' '• PAI: ' '</b>' '<code>' + req()['nomePai'] + '</code>' '\n' + '<b>' '• RAÇA COR: ' '</b>' '<code>' + req()['descricaoRacaCor'] + '</code>' '\n' + '<b>' '• SEXO: ' '</b>' '<code>' + req()['descricaoSexo'] + '</code>' '\n' + '<b>' '• MUNICIPIO NASC: ' '</b>' '<code>' + req()['municipioNasc'] + '</code>' '\n' + '<b>' '• ESTADO NASC: ' '</b>' '<code>' + req()['estadoNasc'] + '</code>' '\n\n' + '<b>' '• LOGRADOURO: ' '</b>' '<code>' + req()['nomeLogradouro'] + '</code>' '\n' + '<b>' '• NÚMERO: ' '</b>' '<code>' + req()['numero'] + '</code>' '\n' + '<b>' '• COMPLEMENTO: ' '</b>' '<code>' + req()['complemento'] + '</code>' '\n' + '<b>' '• BAIRRO: ' '</b>' '<code>' + req()['bairro'] + '</code>' '\n' + '<b>' '• CEP: ' '</b>' '<code>' + req()['numeroCEP'] + '</code>' '\n' + '<b>' '• MUNICIPIO: ' '</b>' '<code>' + req()['nomeMunicipio'] + '</code>' '\n' + '<b>' '• UF: ' '</b>' '<code>' + req()['siglaUF'] + '</code>' '\n' + '<b>' '• ESTADO: ' '</b>' '<code>' + req()['nomeUF'] + '</code>' '\n' + '<b>' '• PAÍS: ' '</b>' '<code>' + req()['nomePais'] + '</code>' '\n\n' + '<b>' '• TELEFONE: ' '</b>' '<code>' + str(reeq['telefone'][0]['numero']) + '</code>' + '\n' + '<b>' '• DD: ' '</b>' '<code>' + str(reeq['telefone'][0]['dd']) + '</code>' + '\n' + '<b>' '• TIPO: ' '</b>' '<code>' + str(reeq['telefone'][0]['tipo']) + '</code>' + '\n\n' + '<b>' '• RG: ' '</b>' '<code>' + str(req()['dadosRg'][0]['numeroIdentidade']) + '</code>' + '\n' + '<b>' '• IDENTIFICADOR: ' '</b>' '<code>' + str(reeq['dadosRg'][0]['identificador'][10:20]) + '</code>' + '\n' + '<b>' '• EXPEDIÇÃO: ' '</b>' '<code>' + str(reeq['dadosRg'][0]['dataExpedicao']) + '</code>' + '\n' + '<b>' '• EMISSOR: ' '</b>' '<code>' + str(reeq['dadosRg'][0]['nomeOrgaoEmissor']) + '</code>' + '\n' + '<b>' '• SIGLA: ' '</b>' '<code>' + str(reeq['dadosRg'][0]['siglaOrgaoEmissor']) + '</code>' + '\n' + '<b>' '• NIS: ' '</b>' '<code>' + str(reeq['dadosRg'][0]['identificadorNis'][9:20]) + '</code>' + '\n' + '<b>' '• DOCUMENTO: ' '</b>' '<code>' + str(reeq['dadosRg'][0]['numeroDocumento']) + '</code>' + '\n\n' + '<b>' '• CERTIDÃO: ' '</b>' '<code>' + str(reeq['dadosCertidao'][0]['identificador'][9:20]) + '</code>' + '\n' + '<b>' '• TIPO: ' '</b>' '<code>' + str(reeq['dadosCertidao'][0]['TipoCertidao']) + '</code>' + '\n' + '<b>' '• CARTORIO: ' '</b>' '<code>' + str(reeq['dadosCertidao'][0]['nomeCartorio']) + '</code>' + '\n' + '<b>' '• LIVRO/FOLHA: ' '</b>' '<code>' + str(reeq['dadosCertidao'][0]['livro']) + '</code>' + '\n' + '<b>' '• TERMO: ' '</b>' '<code>' + str(reeq['dadosCertidao'][0]['termo']) + '</code>' + '\n' + '<b>' '• EMISSÃO: ' '</b>' '<code>' + str(reeq['dadosCertidao'][0]['dataEmissaoCertidao']) + '</code>' + '\n\n' + '<b>' '• GRUPO: @doutrinadorbuscas1' '\n' '• CANAL: @doutrinadorbuscas' '</b>', parse_mode='HTML')
                    hells = bot.reply_to(nome, '<b>' '🚮 CONSULTA SE APAGARÁ EM 1 MINUTO🚮' '</b>', parse_mode='HTML')
                    sleep(60)
                    bot.delete_message(id1, hels.message_id)
                    bot.delete_message(id1, hells.message_id)
                    bot.delete_message(id1, nome.message_id)
                except:
                	bot.reply_to(nome, '<b>' 'SE VOCÊ RECEBEU ESSA MENSAGEM, ESTÁ ERRADO OU VOCÊ JÁ FEZ SUA CONSULTA' '</b>', parse_mode='HTML')
            else:
                		bot.reply_to(nome, '<b>' '✅ Compre acesso com meu pai @Anonylions ✅' '</b>', parse_mode='HTML')
                		
##

session = requests_html.HTMLSession()

##

@bot.message_handler(commands=['verinum'])
def validnum(nome):
            id1 = nome.chat.id

            ltnome = PRIVADO + GRUPO
            if id1 in ltnome:
                try:
                    msg = nome.text
                    fl = msg.split('/cpf')
                    ip = re.sub('[^0-9+]', '', msg)
                    url = requests.get('http://apilayer.net/api/validate?access_key=5c6f98a2e42e805b281f5b1b53df68df&number=' + ip + '&country_code=&format=1')
                    req = url.json
                    bot.reply_to(nome, '<b>' '🔍☂️ CONSULTA REALIZADA ☂️🔎' '</b>' + '\n\n' + '<b>' '• VÁLIDO: ' '</b>' '<code>' + str(req()['valid']) + '</code>' + '\n' + '<b>' '• NÚMERO: ' '</b>' '<code>' + str(req()['international_format']) + '</code>' + '\n' + '<b>' '• CODE PAÍS: ' '</b>' '<code>' + str(req()['country_prefix']) + '</code>' + '\n' + '<b>' '• SIGLA: ' '</b>' '<code>' + str(req()['country_code']) + '</code>' + '\n' + '<b>' '• PAÍS: ' '</b>' '<code>' + str(req()['country_name']) + '</code>' + '\n' + '<b>' '• ESTADO: ' '</b>' '<code>' + str(req()['location']) + '</code>' + '\n' + '<b>' '• OPERADORA: ' '</b>' '<code>' + str(req()['carrier']) + '</code>' + '\n' '<b>' '• TIPO: ' '</b>' '<code>' + str(req()['line_type']) + '</code>' + '\n\n' + '<b>' + '• @Anonylions\n• Anonylions\n• @Anonylions' '</b>' , parse_mode='HTML')
                except:
                 bot.reply_to(nome, '<b>' 'TÁ ERRADO, IDIOTA!' '</b>', parse_mode='HTML')
            else:
                  bot.reply_to(nome, '<b>' '✅ Compre acesso com meu pai @Anonylions ✅' '</b>', parse_mode='HTML')
##

@bot.message_handler(commands=['bin'] + ['BIN'])
def lbz(men):
            notbin = []
            bid = men.chat.id
            cp = men.text
            if bid in notbin:
                bot.reply_to(men, '⚠ 𝙘𝙤𝙣𝙨𝙪𝙡𝙩𝙖 𝙙𝙚 𝙗𝙞𝙣 𝙙𝙚𝙨𝙖𝙩𝙞𝙫𝙖𝙙𝙖 𝙥𝙖𝙧𝙖 𝙚𝙨𝙩𝙚 𝙜𝙧𝙪𝙥𝙤 ⚠')
            else:
                try:
                    bn = re.sub('[^0-9]', '', cp)
                    response = requests.get('https://binlist.io/lookup/{}'.format(bn))
                    res = response.content
                    r = json.loads(res)
                    if str(r['success']) == str('True'):

                        bot.reply_to(men, '\n         ㅤ   ㅤ<b>🔍☂️ DADOS BIN ☂️🔎</b>\n▱▱▱▱▱▱▱▱▱▱▱▱▱\n\n<b>• BIN</b>: ' + '<code>' + str(
                            r['number']['iin']) + '</code>' + '\n' +
                                     '<b>• BANDEIRA</b>: ' + '<code>' + str(r['scheme']) + '</code>' + '\n' +
                                     '<b>• TIPO</b>: ' + '<code>' + str(r['type']) + '</code>' + '\n' +
                                     '<b>• NÍVEL</b>: ' + '<code>' + str(r['category']) + '</code>' + '\n' +
                                     '<b>• BANCO</b>: ' + '<code>' + str(r['bank']['name']) + '</code>' + '\n' +
                                     '<b>• TEL BANCO</b>: ' + '<code>' + str(r['bank']['phone']) + '</code>' + '\n' +
                                     '<b>• URL</b>: ' + str(r['bank']['url']) + '\n' +
                                     '<b>• PAÍS</b>: ' + '<code>' + str(r['country']['name']) + '</code>' + '\n' +
                                     '<b>• ID</b>: ' + '<code>' + str(r['country']['alpha3']) + '</code>' + '\n' +
                                     '<b>• SIGLA</b>: ' + '<code>' + str(r['country'][
                                                               'alpha2']) + '</code>' + '\n' +  '\n▱▱▱▱▱▱▱▱▱▱▱▱▱\n' + '<b>' '• GRUPO: @doutrinadorbuscas1' '\n' '• CANAL: @doutrinadorbuscas' '</b>', parse_mode='HTML')
                    else:
                        bot.reply_to(men, '<b>VEJA O EXEMPLO</b>: "' + '<code>' + '/bin 651652' + '</code>' + '"', parse_mode='HTML')
                except:
                    bot.reply_to(men, '<b>⚠ DIGITE UMA BIN VIADO ⚠</b>', parse_mode='HTML')

##

@bot.message_handler(commands=['cep'] + ['CEP'])
def bno(men):
    notbin = []
    bid = men.chat.id
    mensagem = men.text
    if men.text == '/cep':
        bot.reply_to(men, '<b>' + '⚠ DIGITE UM CEP ⚠' + '</b>', parse_mode='HTML')
    if men.text == '/CEP':
        bot.reply_to(men, '<b>' + '⚠ DIGITE UM CEP ⚠' + '</b>', parse_mode='HTML')
    else:
        try:
        	ipp = re.sub('[^0-9]', '', mensagem)
        	url = requests.get('http://geradorapp.com/api/v1/cep/search/' + ipp + '?token=4f8d9149be4858c837b8b38f5c0d194a')
        	reqi = url.json
        	bot.reply_to(men, '<b>' 'ㅤ🔍☂️ CONSULTA DE CEP ☂️🔎' '</b>' + '\n▱▱▱▱▱▱▱▱▱▱▱▱▱\n\n' + '<b>' '• CEP: ' '</b>' '<code>' + ipp + '</code>' '\n' + '<b>' '• UF: ' '</b>' '<code>' + reqi()['data']['state'] + '</code>' '\n' + '<b>' '• ESTADO: ' '</b>' '<code>' + reqi()['data']['state_name'] + '</code>' '\n' + '<b>' '• CIDADE: ' '</b>' '<code>' + reqi()['data']['city'] + '</code>' '\n\n' + '<b>' '• LOGRADOURO: ' '</b>' '<code>' + reqi()['data']['address'] + '</code>' '\n' + '<b>' '• BAIRRO: ' '</b>' '<code>' + reqi()['data']['district'] + '</code>' '\n' + '<b>' '• NAME: ' '</b>' '<code>' + reqi()['data']['address_name'] + '</code>' '\n' + '<b>' '• IBGE: ' '</b>' '<code>' + reqi()['data']['city_code'] + '</code>' '\n' + '<b>' '• STATUS: ' '</b>' '<code>' + reqi()['data']['status'] + '</code>' '\n' + '<b>' '• MENSAGEM: ' '</b>' '<code>' + reqi()['data']['message'] + '</code>' '\n\n▱▱▱▱▱▱▱▱▱▱▱▱▱\n' + '<b>' '• GRUPO: @doutrinadorbuscas1' '\n' '• CANAL: @doutrinadorbuscas' '</b>', parse_mode='HTML')
        except:
                   bot.reply_to(men, '<b>' + 'SE VOCÊ RECEBEU ESSA MENSAGEM, ESTÁ ERRADO OU VOCÊ JÁ FEZ SUA CONSULTA ;(' + '</b>', parse_mode='HTML')

##

@bot.message_handler(commands=['menu'])
def bniio(men):
    notbin = []
    bid = men.chat.id
    mensagem = men.text
    if men.text == '/menuu':
        bot.reply_to(men, '<b>' + '⚠ ERRADO SEU VIADO ⚠' + '</b>', parse_mode='HTML')
    else:
        try:
        	bot.reply_to(men, '<b>' '🔍☂️ MENU DO BOT☂️ 🔎' '</b>' + '\n\n' + '<b>' '[🌍+] CEP:</b><code> /cep 89874000' '</code>' + '\n' + '<b>' '[💳+] BIN:</b><code> /bin 545323' + '</code>' '\n' + '<b>' '[🇧🇷+] CNPJ:</b><code> /cnpj 27865757000102' + '</code>' '\n' + '<b>' '[🔒+] CPF: ' '</b>''<code>' '/cpf 03655915993' '</code>' + '\n' + '<b>' '[🛡️+] PLACA: ' '</b>' + '<code>' '/placa GTJ6699' '</code>' + '\n\n' + '<b>' '[☂️+] CHK CC: </b><code>/chkcc 6509079001042420' '</code>' '\n\n' + '<b>' '[👥+] GERAR CPF:</b><code> /gencpf' '</code>' + '\n' + '<b>' '[📫+] GERAR EMAIL:</b><code> /genemail' + '</code>' + '\n' + '<b>' '[📪+] GERAR CNPJ:</b><code> /gencnpj' + '</code>' '\n\n' + '<b>' '[⏳+] VALIDAR CPF E NUMERO:</b><code> /validar 036.559.159-93 /verinum +5521974361078'  + '</code>' '\n\n' + '<b>🔛 BY: @Doutrinadornybot</b>' , parse_mode='HTML')
        except:
                    bot.reply_to(men, '<b>' + '.' + '</b>', parse_mode='HTML')

##
@bot.message_handler(commands=['validar'] + ['VALIDAR'])
def bnio(men):
    notbin = []
    bid = men.chat.id
    mensagem = men.text
    if men.text == '/validar':
        bot.reply_to(men, '<b>' + '⚠ DIGITE UM CPF ⚠' + '</b>', parse_mode='HTML')
    if men.text == '/VALIDAR':
        bot.reply_to(men, '<b>' + '⚠ DIGITE UM CPF ⚠' + '</b>', parse_mode='HTML')
    else:
        try:
        	ip = re.sub('[^0-9]', '', mensagem)
        	urrl = requests.get("http://geradorapp.com/api/v1/cpf/validate/" + ip + "?token=4f8d9149be4858c837b8b38f5c0d194a")
        	reeq = urrl.json
        	bot.reply_to(men, '<b>' 'ㅤ🔍☂️ VALIDAR CPF ☂️🔎' + '</b>' +'\n▱▱▱▱▱▱▱▱▱▱▱\n\n' + '<b>' + '• CPF: ' + '</b>' + '<code>' + reeq()['data']['number_formatted'] + '</code>' + '\n' + '<b>' + '• NOME: ' + '</b>' + '<code>' + 'N/A' + '</code>' + '\n' + '<b>' + '• SITUAÇÃO: ' + '</b>' + '<code>' + reeq()['data']['message'] + '</code>' + '\n\n▱▱▱▱▱▱▱▱▱▱▱\n' + '<b>' '• GRUPO: @doutrinadorbuscas1' '\n' '• CANAL: @doutrinadorbuscas' '</b>', parse_mode='HTML')
        except:
                    bot.reply_to(men, '<b>' + 'OPS, CPF INVÁLIDO OU NÃO ENCONTRADO! :(' + '</b>', parse_mode='HTML')

##

@bot.message_handler(commands=['cnpj'] + ['CNPJ'])
def bnioo(men):
    notbin = []
    bid = men.chat.id
    mensagem = men.text
    if men.text == '/cnpj':
        bot.reply_to(men, '⚠ 𝘿𝙄𝙂𝙄𝙏𝙀 𝙐𝙈 𝘾𝙉𝙋𝙅, 𝙄𝘿𝙄𝙊𝙏𝘼 ⚠')
    if men.text == '/CNPJ':
        bot.reply_to(men, '⚠ 𝘿𝙄𝙂𝙄𝙏𝙀 𝙐𝙈 𝘾𝙉𝙋𝙅, 𝙄𝘿𝙄𝙊𝙏𝘼 ⚠')
    else:
        try:
        	ip = re.sub('[^0-9]', '', mensagem)
        	
        	header = {"Authorization": "Bearer NU.FRdMl435cce2f04022699c735c1449c5ee472d6ed166a8b4087525abf7c47590e4723"}
        	
        	url = requests.get('https://api.nudata.com.br/receita/{}'.format(ip), headers=header)
        	o = url.text
        	req = json.loads(o)
        
        	bot.reply_to(men, 'ㅤㅤㅤㅤㅤ🔍 ☂️𝘿𝘼𝘿𝙊𝙎 𝘾𝙉𝙋𝙅☂️ 🔎' +
'▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱\n𝘾𝙉𝙋𝙅: ' '<code>' + str(req['result']['cnpj']) + '</code>' '\n▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱\n𝙏𝙄𝙋𝙊: ' '<code>' + str(req['result']['tipo']) + '</code>' '\n▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱\n' +
                     '𝙉𝙊𝙈𝙀: ' '<code>' + str(req['result']['nome']) + '</code>' '\n▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱\n' +
                     '𝙏𝙀𝙇𝙀𝙁𝙊𝙉𝙀𝙎: ' '<code>' + str(req['result']['telefone']) + '</code>' '\n▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱\n' +
                     '𝙀𝙈𝘼𝙄𝙇: ' '<code>' + str(req['result']['email']) + '</code>' '\n▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱\n' +
                     '𝙎𝙄𝙏𝙐𝘼𝘾̧𝘼̃𝙊: ' '<code>' + str(req['result']['situacao']) + '</code>' '\n▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱\n' +
                     '𝙇𝙊𝙂𝙍𝘼𝘿𝙊𝙐𝙍𝙊: ' '<code>' + str(req['result']['logradouro']) + '</code>' '\n▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱\n' +
                     '𝘽𝘼𝙄𝙍𝙍𝙊: ' '<code>' + str(req['result']['bairro']) + '</code>' '\n▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱\n' +
                     '𝙉𝙐́𝙈𝙀𝙍𝙊: ' '<code>' + str(req['result']['numero']) + '</code>' '\n▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱\n' + 
                     '𝘾𝙀𝙋: ' '<code>' + str(req['result']['cep']) + '</code>' '\n▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱\n' + 
                     '𝙈𝙐𝙉𝙄𝘾𝙄́𝙋𝙄𝙊: ' '<code>' + str(req['result']['cidade']) + '</code>' '\n▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱\n'
                     '𝙋𝙊𝙍𝙏𝙀: ' '<code>' + str(req['result']['porte']) + '</code>' '\n▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱\n' +
                     '𝘼𝘽𝙀𝙍𝙏𝙐𝙍𝘼: ' '<code>' + str(req['result']['dataAbertura']) + '</code>' '\n▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱\n' +
                     '𝙁𝘼𝙉𝙏𝘼𝙎𝙄𝘼: ' '<code>' + str(req['result']['nomeFantasia']) + '</code>' '\n▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱\n' +
                     '𝙎𝙏𝘼𝙏𝙐𝙎: ' '<code>' + str(req['status']) + '</code>' '\n▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱\n' +
                     '𝘾𝘼𝙋𝙄𝙏𝘼𝙇: ' '<code>' + str(req['result']['capitalSocial']) + '</code>' '\n▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱\n'
                     '𝘼𝙏𝙄𝙑𝙄𝘿𝘼𝘿𝙀 𝙋𝙍𝙄𝙉𝘾𝙄𝙋𝘼𝙇: ' '<code>' + str(req['result']['atividadePrimaria']) + '</code>' '\n▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱\n' +
                     '𝘼𝙏𝙄𝙑𝙄𝘿𝘼𝘿𝙀 𝙎𝙀𝘾𝙐𝙉𝘿𝘼́𝙍𝙄𝘼: ' '<code>' + str(req['result']['atividadeSecundaria']) + '</code>' '\n▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱\n' +
                     '𝘿𝘼𝙏𝘼 𝙎𝙄𝙏𝙐𝘼𝘾̧𝘼̃𝙊: ' '<code>' + str(req['result']['dataSituacao']) + '</code>' '\n▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱\n' + '𝙐𝙁: ' '<code>' + str(req['result']['estado']) + '</code>' '\n▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱\n' + '𝘿𝙊𝙉𝙊𝙎: ' '<code>' + str(req['result']['qsa']) + '</code>'  '\n▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱\n𝙂𝙍𝙐𝙋𝙊:  @doutrinadorbuscas1\n𝘾𝘼𝙉𝘼𝙇:  @doutrinadorbuscas', parse_mode='HTML')
        except:
                     	bot.reply_to(men, '𝙊𝙋𝙎, 𝘾𝙉𝙋𝙅 𝙉𝘼̃𝙊 𝙀𝙉𝘾𝙊𝙉𝙏𝙍𝘼𝘿𝙊 𝙂𝘼𝘿𝙊 🐂')

##

@bot.message_handler(commands=['chkcc'])
def zion(nome):
            id1 = nome.chat.id

            ltnome = PRIVADO + GRUPO
            if id1 in ltnome:
                try:
                    msg = nome.text
                    fl = msg.split('/cpf')
                    ipo = re.sub('[^0-9|]', '', msg)
                    url = requests.get('https://lookup.binlist.net/' + ipo)
                    req = url.json
                    bot.reply_to(nome, '<b>' 'ㅤㅤㅤ✅☂️ CC CHECKER ☂️✅' '</b>' + '\n▱▱▱▱▱▱▱▱▱▱▱▱▱▱\n\n' + '<b>' '• APROVADO ' + ' ✅' + '\n\n' + '• BANDEIRA: ' '</b>' '<code>' + req()['scheme'] + '</code>' '\n' + '<b>' '• TIPO: ' '</b>' '<code>' + req()['type'] + '</code>' '\n' + '<b>' '• PAÍS: ' '</b>' '<code>' + str(req()['country']['name']) + '</code>' '\n' + '<b>' '• BANCO: ' '</b>' '<code>' + req()['bank']['name'] + '</code>' '\n\n' + '<b>' '• CC: ' '</b>' '<code>' + ipo + '</code>' '\n\n▱▱▱▱▱▱▱▱▱▱▱▱▱▱\n' + '<b>' '• CHK BY: @Doutrinadornybot''</b>', parse_mode='HTML')
                except:
                	bot.reply_to(nome, '<b>' '#Reproved ' + ipo + ' ❌' '</b>', parse_mode='HTML')
            else:
                		bot.reply_to(nome, '<b>' '✅ Compre acesso com meu pai @Anonylions✅' '</b>', parse_mode='HTML')

##

@bot.message_handler(commands=['gencpf'])
def lbx(men):
    notbin = []
    bid = men.chat.id
    mensagem = men.text
    if men.text == '/validar':
        bot.reply_to(men, '<b>' + '⚠ ⚠' + '</b>', parse_mode='HTML')
    else:
        try:
        	ip = re.sub('[^0-9]', '', mensagem)
        	url = requests.get('http://geradorapp.com/api/v1/cpf/generate?token=4f8d9149be4858c837b8b38f5c0d194a')
        	respostaa = url.json
        	resposta = respostaa()['data']['number_formatted']
        	url = requests.get('http://geradorapp.com/api/v1/cpf/generate?token=4f8d9149be4858c837b8b38f5c0d194a')
        	respostaa = url.json
        	cpff = respostaa()['data']['number_formatted']
        	url = requests.get('http://geradorapp.com/api/v1/cpf/generate?token=4f8d9149be4858c837b8b38f5c0d194a')
        	respostaa = url.json
        	dkzinn = respostaa()['data']['number_formatted']
        	url = requests.get('http://geradorapp.com/api/v1/cpf/generate?token=4f8d9149be4858c837b8b38f5c0d194a')
        	respostaa = url.json
        	lbx = respostaa()['data']['number_formatted']
        	url = requests.get('http://geradorapp.com/api/v1/cpf/generate?token=4f8d9149be4858c837b8b38f5c0d194a')
        	respostaa = url.json
        	lb = respostaa()['data']['number_formatted']
        	url = requests.get('http://geradorapp.com/api/v1/cpf/generate?token=4f8d9149be4858c837b8b38f5c0d194a')
        	respostaa = url.json
        	lbzinn = respostaa()['data']['number_formatted']
        	url = requests.get('http://geradorapp.com/api/v1/cpf/generate?token=4f8d9149be4858c837b8b38f5c0d194a')
        	respostaa = url.json
        	dkz = respostaa()['data']['number_formatted']
        	url = requests.get('http://geradorapp.com/api/v1/cpf/generate?token=4f8d9149be4858c837b8b38f5c0d194a')
        	respostaa = url.json
        	andrei = respostaa()['data']['number_formatted']
        	url = requests.get('http://geradorapp.com/api/v1/cpf/generate?token=4f8d9149be4858c837b8b38f5c0d194a')
        	respostaa = url.json
        	pc = respostaa()['data']['number_formatted']
        	url = requests.get('http://geradorapp.com/api/v1/cpf/generate?token=4f8d9149be4858c837b8b38f5c0d194a')
        	respostaa = url.json
        	gamer = respostaa()['data']['number_formatted']
        	bot.reply_to(men, '<b>' 'ㅤ⚙ ☂️ GERADOR DE CPF ☂️⚙' '</b>' + '\n▱▱▱▱▱▱▱▱▱▱▱▱▱\n\n' + '<b>' '• CPF: ' '</b>''<code>' + resposta + '</code>' + '\n' + '<b>' '• CPF: ' '</b>' '<code>' + cpff + '</code>' + '\n' + '<b>' + '• CPF: ' + '</b>' '<code>' + dkzinn + '</code>' + '\n' + '<b>' '• CPF: ' '</b>''<code>' + lbx + '</code>' + '\n' + '<b>' '• CPF: ' '</b>''<code>' + lb + '</code>' + '\n' + '<b>' '• CPF: ' '</b>''<code>' + lbzinn + '</code>' + '\n' + '<b>' '• CPF: ' '</b>''<code>' + dkz + '</code>' + '\n' + '<b>' '• CPF: ' '</b>''<code>' + andrei + '</code>' + '\n' + '<b>' '• CPF: ' '</b>''<code>' + pc + '</code>' + '\n' + '<b>' '• CPF: ' '</b>''<code>' + gamer + '</code>' + '\n\n▱▱▱▱▱▱▱▱▱▱▱▱▱\n' + '<b>' '• GRUPO: @doutrinadorbuscas1' '\n' '• CANAL: @doutrinadorbuscas' '</b>', parse_mode='HTML')
        except:
                    bot.reply_to(men, '.')

##

@bot.message_handler(commands=['gencnpj'])
def lbxk(men):
    notbin = []
    bid = men.chat.id
    mensagem = men.text
    if men.text == '/validar':
        bot.reply_to(men, '<b>' + '⚠ ⚠' + '</b>', parse_mode='HTML')
    else:
        try:
        	ip = re.sub('[^0-9]', '', mensagem)
        	url = requests.get('http://geradorapp.com/api/v1/cnpj/generate?token=4f8d9149be4858c837b8b38f5c0d194a')
        	respostaa = url.json
        	respostak = respostaa()['data']['number_formatted']
        	url = requests.get('http://geradorapp.com/api/v1/cnpj/generate?token=4f8d9149be4858c837b8b38f5c0d194a')
        	respostaa = url.json
        	cpffk = respostaa()['data']['number_formatted']
        	url = requests.get('http://geradorapp.com/api/v1/cnpj/generate?token=4f8d9149be4858c837b8b38f5c0d194a')
        	respostaa = url.json
        	dkzinnk = respostaa()['data']['number_formatted']
        	url = requests.get('http://geradorapp.com/api/v1/cnpj/generate?token=4f8d9149be4858c837b8b38f5c0d194a')
        	respostaa = url.json
        	lbxk = respostaa()['data']['number_formatted']
        	url = requests.get('http://geradorapp.com/api/v1/cnpj/generate?token=4f8d9149be4858c837b8b38f5c0d194a')
        	respostaa = url.json
        	lbk = respostaa()['data']['number_formatted']
        	url = requests.get('http://geradorapp.com/api/v1/cnpj/generate?token=4f8d9149be4858c837b8b38f5c0d194a')
        	respostaa = url.json
        	lbzinnk = respostaa()['data']['number_formatted']
        	url = requests.get('http://geradorapp.com/api/v1/cnpj/generate?token=4f8d9149be4858c837b8b38f5c0d194a')
        	respostaa = url.json
        	dkzk = respostaa()['data']['number_formatted']
        	url = requests.get('http://geradorapp.com/api/v1/cnpj/generate?token=4f8d9149be4858c837b8b38f5c0d194a')
        	respostaa = url.json
        	andreik = respostaa()['data']['number_formatted']
        	url = requests.get('http://geradorapp.com/api/v1/cnpj/generate?token=4f8d9149be4858c837b8b38f5c0d194a')
        	respostaa = url.json
        	pck = respostaa()['data']['number_formatted']
        	url = requests.get('http://geradorapp.com/api/v1/cnpj/generate?token=4f8d9149be4858c837b8b38f5c0d194a')
        	respostaa = url.json
        	gamerk = respostaa()['data']['number_formatted']
        	bot.reply_to(men, '<b>' 'ㅤ⚙ ☂️GERADOR DE CNPJ ☂️⚙' '</b>' + '\n▱▱▱▱▱▱▱▱▱▱▱▱▱▱\n\n' + '<b>' '• CNPJ: ' '</b>''<code>' + respostak + '</code>' + '\n' + '<b>' '• CNPJ: ' '</b>' '<code>' + cpffk + '</code>' + '\n' + '<b>' + '• CNPJ: ' + '</b>' '<code>' + dkzinnk + '</code>' + '\n' + '<b>' '• CNPJ: ' '</b>''<code>' + lbxk + '</code>' + '\n' + '<b>' '• CNPJ: ' '</b>''<code>' + lbk + '</code>' + '\n' + '<b>' '• CNPJ: ' '</b>''<code>' + lbzinnk + '</code>' + '\n' + '<b>' '• CNPJ: ' '</b>''<code>' + dkzk + '</code>' + '\n' + '<b>' '• CNPJ: ' '</b>''<code>' + andreik + '</code>' + '\n' + '<b>' '• CNPJ: ' '</b>''<code>' + pck + '</code>' + '\n' + '<b>' '• CNPJ: ' '</b>''<code>' + gamerk + '</code>' + '\n\n▱▱▱▱▱▱▱▱▱▱▱▱▱▱\n' + '<b>' '• GRUPO: @doutrinadorbuscas1' '\n' '• CANAL: @doutrinadorbuscas' '</b>', parse_mode='HTML')
        except:
                    bot.reply_to(men, '.')

####

@bot.message_handler(commands=['genemail'])
def ipoop(men):
    notbin = []
    bid = men.chat.id
    mensagem = men.text
    if men.text == '/chkcc':
        bot.reply_to(men, '<b>' '⚠' '</b>', parse_mode='HTML')
    else:
        try:
        	ipo = re.sub('[^A-Z]', '', mensagem)
        	url = requests.get('https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1')
        	url2 = requests.get('https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1')
        	url3 = requests.get('https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1')
        	req = url.text
        	req2 = url2.text
        	req3 = url3.text
        	bot.reply_to(men, '<b>' '📧 ☂️EMAIL FAKE ☂️📧' '</b>' + '\n\n' + '<code>' + req + '</code>' + '\n' + '<code>' + req2 + '</code>' + '\n' + '<code>' + req3 + '</code>' + '\n\n' + '<b>' '• GRUPO: @doutrinadorbuscas1' '\n' '• CANAL: @doutrinadorbuscas' '</b>', parse_mode='HTML')
        except:
                    bot.reply_to(men, '', parse_mode='HTML')

####

@bot.message_handler(commands=['placa'])
def zbsn(nome):
            id1 = nome.chat.id

            ltnome = PRIVADO + GRUPO
            if id1 in ltnome:
                try:
                    msg = nome.text
                    fl = msg.split('/placa')
                    ipp = re.sub('[^A-Z]', '', msg)
                    ip = re.sub('[^0-9]', '', msg)
                    url = requests.get("https://apicarros.com/v1/consulta/" + ipp + ip + "/json", verify=False)
                    req = url.json()
                    helss = bot.reply_to(nome, '<b>' '🔍☂️ CONSULTA REALIZADA ☂️🔎' '</b>' + '\n\n' + '<b>' '• PLACA: ' '</b>''<code>' + req['placa'] + '</code>' + '\n' + '<b>' '• ANO: ' '</b>''<code>' + req['ano'] + '</code>' + '\n' + '<b>' '• CHASSI: ' '</b>''<code>' + req['chassi'] + '</code>' + '\n' + '<b>' '• COR: ' '</b>''<code>' + req['cor'] + '</code>' + '\n' + '<b>' '• DATA: ' '</b>''<code>' + req['data'] + '</code>' + '\n' + '<b>' '• ALARME: ' '</b>''<code>' + req['dataAtualizacaoAlarme'] + '</code>' + '\n' + '<b>' '• VEÍCULO: ' '</b>''<code>' + req['dataAtualizacaoCaracteristicasVeiculo'] + '</code>' + '\n' + '<b>' '• ROUBO/FURTO: ' '</b>''<code>' + req['dataAtualizacaoRouboFurto'] + '</code>' + '\n\n' + '<b>' '• MARCA: ' '</b>''<code>' + req['marca'] + '</code>' + '\n' + '<b>' '• MODELO: ' '</b>''<code>' + req['modelo'] + '</code>' + '\n\n' + '<b>' '• MUNICÍPIO: ' '</b>''<code>' + req['municipio'] + '</code>' + '\n' + '<b>' '• UF: ' '</b>''<code>' + req['uf'] + '</code>' + '\n\n' + '<b>' '• SITUAÇÃO: ' '</b>''<code>' + req['situacao'] + '</code>' + '\n\n' + '<b>' '• GRUPO: @doutrinadorbuscas1' '\n' '• CANAL: @doutrinadorbuscas' '</b>',parse_mode='HTML')
                    hellss = bot.reply_to(nome, '<b>' '🚮 CONSULTA SE APAGARÁ EM 5 MINUTOS🚮' '</b>', parse_mode='HTML')
                    sleep(300)
                    bot.delete_message(id1, helss.message_id)
                    bot.delete_message(id1, hellss.message_id)
                    bot.delete_message(id1, nome.message_id)
                except:
                	bot.reply_to(nome, '<b>' 'SE VOCÊ RECEBEU ESSA MENSAGEM, ESTÁ ERRADO OU VOCÊ JÁ FEZ SUA CONSULTA' '</b>', parse_mode='HTML')
            else:
                		bot.reply_to(nome, '<b>' '✅ Compre acesso com meu pai @Anonylions✅' '</b>', parse_mode='HTML')

####

@bot.message_handler(commands=['dados'])
def boavinnda(message1):
    bot.reply_to(message1, '<b>' '• SEU ID: ' '</b>''<code>' + str(message1.chat.id) + '</code>' '\n'+ '<b>' '• NOME: ' '</b>' '<code>'+ message1.chat.first_name + '</code>' '\n' + '<b>''• USERNAME: '+'@'+message1.chat.username + '</b>' , parse_mode='HTML')

bot.polling()