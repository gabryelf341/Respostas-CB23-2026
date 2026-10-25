"""Seus testes do Marco 1 (veja a seção 6 do ENUNCIADO_MARCO1.md).

Regras: pelo menos 8 testes seus (o exemplo abaixo não conta), uma docstring em cada teste
dizendo qual caso ele cobre, e floats comparados com assertAlmostEqual ou np.allclose.
"""
import unittest

from elevatoria.dados import por_tag
from elevatoria.serie import SerieTemporal


class TestPorTagExemplo(unittest.TestCase):
    """Exemplo do formato. `por_tag` é código existente da base."""

    def test_lista_vazia(self):
        """Sem registros, por_tag devolve uma lista vazia."""
        self.assertEqual(por_tag([], "PT101"), [])


# Acrescente abaixo as suas classes de teste, começando pelos testes de regressão da
# issue #4 (escreva-os ANTES de corrigir o defeito e confirme que falham).
class Test_media_movel(unittest.TestCase):
     def test_quantidade_de_valores(self):
        """Verifica se uma janela de 30 gera 571 médias para 600 leituras."""
        dados = SerieTemporal.de_lista(list(range(600)))

        resultado = SerieTemporal.media_movel(dados, 30)

        self.assertEqual(len(resultado), 571)


if __name__ == "__main__":
    unittest.main()