from models.User import  salvarUsuario, listagemTodosUsuarios, removerUsuario

def salvarUsuarioService(usuario):
    if 'email' not in usuario or 'senha' not in usuario or 'cpf' not in usuario:    #se estiver falntando algum dado vai retornar um erro
        raise ValueError("Todos os campos são obrigatórios!")
    return salvarUsuario(usuario)

def listarTodosUsuariosService():
    return listagemTodosUsuarios()

def removerUmUsuarioService(id):
    return removerUsuario(id)