# Teste os seguintes retornos da classe abaixo
# 
class ClasseDeTreino:

    def retornando_uma_lista(self):
        return []

    def retornando_uma_tupla(self):
        return ()

    def retornando_um_dicionario(self):
        return {}

    def retorando_uma_string(self):
        return "String"
    
    def retornando_um_integer(self):
        return 1

    def retornando_um_float(self):
        return 12.5

    def retornando_um_boolean(self):
        return True
# Exemplo:
# self.assertIsInstance(ClasseDeTreino().retornando_um_boolean(), bool)
# self.assertEqual(ClasseDeTreino().retornando_um_boolean(), True)