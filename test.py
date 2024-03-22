import unittest
from unittest.mock import Mock
import modelo, datetime
from datetime import datetime, date

class ServicoVeiculoTest(unittest.TestCase):

  def setUp(self):
    self.servico = modelo.ServicoVeiculo()
    self.servico.daoCompra = Mock()
    self.servico.daoVenda = Mock()

  def test_isEmPosseDaLoja_1(self):
    # teste: sem data de compra e venda
    
    #preparação  
    servico = modelo.ServicoVeiculo()
    servico.daoCompra = Mock()
    servico.daoVenda = Mock()
    
    #execução 
    placa = "NNX2015"
    servico.daoCompra.getUltimaData.return_value = None #setando None como valores padrões.
    servico.daoVenda.getUltimaData.return_value = None #setando None como valores padrões.
    em_posse = servico.isEmPosseDaLoja(placa)
    
    #avaliação
    self.assertFalse(em_posse)
    
  def test_isEmPosseDaLoja_2(self):
    # teste: com data de compra e sem data de venda
    placa = "NNX2015"
    self.servico.daoCompra.getUltimaData.return_value = datetime(2022, 10, 21)
    self.servico.daoVenda.getUltimaData.return_value = None
    em_posse = self.servico.isEmPosseDaLoja(placa)
    self.assertTrue(em_posse)
    
  def test_isEmPosseDaLoja_3(self):
    # teste: com data de compra e data de venda
    placa = "NNX2015"
    self.servico.daoCompra.getUltimaData.return_value = datetime(2022, 10, 21)
    self.servico.daoVenda.getUltimaData.return_value = datetime(2022, 10, 22)
    em_posse = self.servico.isEmPosseDaLoja(placa)
    self.assertFalse(em_posse)
     
  def test_isEmPosseDaLoja_4(self):
    # teste: com data de compra e sem data de venda
    placa = "NNX2015"
    self.servico.daoCompra.getUltimaData.return_value = datetime(2022, 10, 21)
    self.servico.daoVenda.getUltimaData.return_value = datetime(2021, 10, 22)
    em_posse = self.servico.isEmPosseDaLoja(placa)
    self.assertTrue(em_posse)    

  def test_compra_falha(self):
    placa = "NNX2015"
    data_compra = self.servico.daoCompra.getUltimaData.return_value = datetime(2022, 10, 21)
    self.servico.daoVenda.getUltimaData.return_value = None
    estado_do_veiculo = self.servico.compra(placa, data_compra)
    self.assertFalse(estado_do_veiculo)

  def test_compra_sucesso(self):
    placa = "NNX2015"
    data_compra = self.servico.daoCompra.getUltimaData.return_value = None
    self.servico.daoVenda.getUltimaData.return_value = None
    retorno = self.servico.compra(placa, data_compra)
    print(retorno)
if __name__ == '__main__':
  unittest.main()
