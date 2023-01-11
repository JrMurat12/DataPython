from datetime import datetime, timedelta

class Datas_Br:
    def __init__(self):
        self.momento_cadastro = datetime.today()
        
    def __str__(self):
        return self.format_data()
        
    def mes_cadastro(self):
        meses_do_ano=[
            "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
            "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro" 
        ]
        mes_cadastro = self.momento_cadastro.month - 1
        return meses_do_ano[mes_cadastro]
    
    def dia_semana(self):
        dia_da_semana=[
            "Segunda", "Terça", "Quarta", "Quinta",
            "Sexta", "Sábado", "Domingo"
        ]
        dia_semana = self.momento_cadastro.weekday()
        return dia_da_semana[dia_semana]
    
    def format_data(self):
        data_formatada = self.momento_cadastro.strftime("%d/%m/%Y %H:%M")
        return data_formatada
    
    def tempo_cadastro(self):
        tempo_cadastro = datetime.today() + timedelta(days=15, minutes=20, seconds=30)
        return tempo_cadastro - self.momento_cadastro