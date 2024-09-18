from models.User import  salvarUsuario, listagemTodosUsuarios, removerUsuario

def salvarUsuarioService(nome, email, senha, cpf):
    return salvarUsuario(nome, email, senha, cpf)

def listarTodosUsuariosService():
    return listagemTodosUsuarios()

def removerUmUsuarioService(id):
    return removerUsuario(id)

def atualizarUsuarioService():
    pass