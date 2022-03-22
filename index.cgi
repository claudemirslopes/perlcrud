#!/usr/bin/perl

use CGI;
use CGI::Carp qw(fatalsToBrowser);
use Encode qw(decode encode);

$BASEAPP = $ENV{HTTP_BASEAPP};

$cgi = new CGI->new;
print $cgi->header(-charset => 'utf-8');

require $BASEAPP."/GLOBAL/cgi-local/modulos/kernel/000.cgi";
use strict;
use CGI ':standard';
use lib "controllers"; 

use Testes;

print <<HTML;
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lista de Teste [Claudemir]</title>
    <!-- CSS, Bootstrap -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap\@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">
    <!-- Sweet Alert -->
    <link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/sweetalert/1.1.3/sweetalert.min.css">
</head>
<body style="margin-top:55px;">
    <div class="container">
        <script>
            function confirmExcluir(id)
                {
                swal({
                    title: "Excluir",
                    text: "Confirma a exclusão do registro?",
                    type: "error",
                    showCancelButton: true,
                    confirmButtonClass: 'btn-success',
                    confirmButtonText: 'Sim',
                    cancelButtonText: 'Não',
                    closeOnConfirm: false
                }, function () {
                    window.location.href = 'Views/excluir.cgi?del_id=' + id;   
                });
                }
        </script>
        <div class="card">
            <div class="card-header bg-secondary text-light">
                <div class="row">
                    <div class="col-md-8">
                        <h4>Lista de Registros</h4>
                    </div>
                    <!--<div class="col-md-2">
                        <a href='Views/cadastrar.cgi' class='btn btn-warning btn-sm float-right'><i class="fa fa-plus" aria-hidden="true"></i>&nbsp; Adicionar registro</a>
                    </div>-->
                    <div class="col-md-4">
                        <a href="javascript:;" class="btn btn-warning btn-sm float-right" data-toggle="modal" data-target="#addRegModal"><i class="fa fa-plus" aria-hidden="true"></i>&nbsp; Adicionar registro</a>
                    </div>
                </div>
            </div>
            <div class="card-body">
                <table class='table table-striped table-sm'>
                    <tr>
                        <th style="display:none;">ID</th>
                        <th>Nome</th>
                        <th>E-mail</th>
                        <th>Usuario</th>
                        <th style="text-align:right;">Ações</th>
                    </tr>
HTML


my $testes = Testes->new();
my $con01 = $testes->getAll();

#Listar registros do banco de dados
while (my @data = $con01->fetchrow_array()) {
my $id = $data[0];
my $nome = $data[1];
my $email = $data[2];
my $usuario = $data[3];

print qq~
                    <tr>
                        <td style='display:none;'>$id</td>
                        <td>$nome</td>
                        <td>$email</td>
                        <td>$usuario</td>
                        <td style="text-align:right;">
                            <a href="javascript:;" onclick="editarRegistro($id)" title="Editar" class="text-primary"><i class="fa fa-pencil-square-o"></i></a>&nbsp;
                            <a class='text-danger' href="javascript:;" onclick="confirmExcluir($id)"><i class="fa fa-trash" aria-hidden="true"></i></a>
                        </td>
                    </tr>
    ~;

}



print <<HTML;
            </table>
            </div>
        </div>
    </div>
    <!-- Modal Adicionar Registro -->
    <div id="addRegModal" class="modal fade" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog modal-lg" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="addRegModalLabel">Cadastrar Registro</h5>
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                <div class="modal-body">
                    <form id="insert_form" action="processa/adiciona_cadastro.cgi" method="POST">
                        <div class="form-group mb-2">
                            <label for="nome">Nome</label>
                            <input type="text" class="form-control" id="nome" name="nome" aria-describedby="nome" placeholder="Nome completo">
                        </div>
                        <div class="form-group mb-2">
                            <label for="email">E-mail</label>
                            <input type="text" class="form-control" id="email" name="email" aria-describedby="email" placeholder="E-mail válido">
                        </div>
                        <div class="form-group mb-2">
                            <label for="usuario">Usuário</label>
                            <input type="text" class="form-control" id="usuario" name="usuario" aria-describedby="usuario" placeholder="Usuário">
                        </div>
                        <input type="hidden" id="senha"  value="hhfjsdḧghg*&uj" name="senha">
                        <div class="form-group mt-4">
                            <input class="btn btn-info" type="submit" name="CadReg" id="CadReg"  value="Cadastrar registro" style="float:right;">
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
    <!-- Modal Editar Registro -->
    <div id="ModalRegistro" class="modal fade" role="dialog">
        <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">Editar Registro</h5>
            <button class="close" type="button" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">×</span>
            </button>
            </div>
            <div class="modal-body"></div>
        </div>
        </div>
    </div>
    <script>
        /* ===================================== */
        /* AJAX MODAL EDITAR/EXCLUÍR (Registro) */
        /* =================================== */
        function editarRegistro(id) {
            
            \$.ajax({
                url: "Views/editar.cgi",
                type:'POST',
                data:{id:id},
                beforeSend:function(){
                    \$('#ModalRegistro').find('.modal-body').html('<center><img src="#"></center>');
                    \$('#ModalRegistro').modal('show');
                },
                success:function(html){
                    \$('#ModalRegistro').find('.modal-body').html(html);

                    \$('#ModalRegistro').modal('show');
                }
            });
        }
    </script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
    <!-- JavaScript, Bootstrap -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap\@4.5.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ho+j7jyWK8fNQe+A12Hb8AhRq26LrZ/JpcUGGOn+Y7RsweNrtN/tE3MoK7ZeZDyx" crossorigin="anonymous"></script>
    <!-- Font Awesome -->
    <script src="https://kit.fontawesome.com/a8568f4b07.js" crossorigin="anonymous"></script>
    <!-- Sweet Alert -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/sweetalert/1.1.3/sweetalert.min.js"></script>
</body>
</html>
HTML


