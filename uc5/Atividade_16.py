class Pokemon:
    def _init_(self, nome, hp, iv, tipos, ataqueRapido, ataquesCarregados):
        self.nome = nome
        self.hp = hp
        self.iv = iv
        self.tipos = tipos
        self.ataqueRapido = ataqueRapido
        self.energiaAcumulada = 0
        self.ataquesCarregados = ataquesCarregados

    def atacar(self, alvo, ataque):
        dano = (ataque.dano * self.iv) / 65
        print(f"{self.nome} usou {ataque.nome} em {alvo.nome} e causou {dano} de dano.")
        self.energiaAcumulada += ataque.geraEnergia
        print(f"{self.nome} acumulou {ataque.geraEnergia} de energia.")
        alvo.hp -= dano
        if alvo.hp <= 0:
            print(f"{alvo.nome} foi derrotado!")
            return True  # Retorna True se o alvo foi derrotado
        return False

    def _str_(self):
        return f"Nome: {self.nome}, HP: {self.hp}"

class Ataque:
    def _init_(self, nome, dano, tipo, geraEnergia):
        self.nome = nome
        self.dano = dano
        self.tipo = tipo
        self.geraEnergia = geraEnergia

    def _str_(self):
        return f"Nome: {self.nome}, Dano: {self.dano}, Tipo: {self.tipo}, Geração de Energia: {self.geraEnergia}"

class AtaqueCarregado(Ataque):
    def _init_(self, nome, dano, tipo, geraEnergia):
        super()._init_(nome, dano, tipo, geraEnergia)


nevasca = AtaqueCarregado("Nevasca", 140, "Gelo", 65)
jato_de_agua = AtaqueCarregado("Jato de Água", 30, "Água", 75)
meteoro_do_dragao = AtaqueCarregado("Meteoro do Dragão", 150, "Dragão", 65)
garra_de_dragao = AtaqueCarregado("Garra de Dragão", 160, "Dragão", 70)


kyogre = Pokemon("Kyogre", 200, 45, ["Água"], jato_de_agua, [nevasca, jato_de_agua])
dragonite = Pokemon("Dragonite", 200, 44, ["Dragão", "Voador"], garra_de_dragao, [meteoro_do_dragao, garra_de_dragao])


while kyogre.hp > 0 and dragonite.hp > 0:
    kyogre.atacar(dragonite, kyogre.ataqueRapido)
    if dragonite.hp <= 0:
        break 
    dragonite.atacar(kyogre, dragonite.ataqueRapido)
    if kyogre.hp <= 0:
        break  


if kyogre.hp > 0:
    print(f"{kyogre.nome} venceu a batalha!")
else:
    print(f"{dragonite.nome} venceu a batalha!")