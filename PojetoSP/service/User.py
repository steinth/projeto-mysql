from models.User import  atualizarUmUsuario, buscarPorId, exibirInformacoesUsuario, salvarUsuario, listagemTodosUsuarios, removerUsuario

def salvarUsuarioService(nome, email, senha, cpf):
    return salvarUsuario(nome, email, senha, cpf)

def listarTodosUsuariosService():
    return listagemTodosUsuarios()

def removerUmUsuarioService(id):
    return removerUsuario(id)

def atualizarUsuarioService(id, nome, email, cpf):
    #return atualizarUmUsuario(id, nome, email, cpf)
    pass 

def buscarPorIdService(id):
    return buscarPorId(id)

def exibirInformacoesService(id):
    return buscarPorId(id)