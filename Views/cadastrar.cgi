#!/usr/bin/perl

use CGI;
use CGI::Carp qw(fatalsToBrowser);
use Encode qw(decode encode);


$cgi = new CGI->new;
print $cgi->header(-charset => 'utf-8');


print <<HTML 
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cadastro de Teste [Claudemir]</title>
    <!-- CSS, Bootstrap -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap\@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">
</head>
<body style="margin-top:55px;">
    <div class="container">
        <div class="card">
            <div class="card-header bg-secondary text-light">
                <h4>Cadastrar Registro <a class='btn btn-outline-warning btn-sm' href='../index.cgi' style='float:right;'><i class="fa fa-angle-double-left" aria-hidden="true"></i></a></h4>
            </div>
            <div class="card-body">
                <form action="../processa/adiciona_cadastro.cgi" method="POST">
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
                    <input type="hidden" value="hhfjsdḧghg*&uj" name="senha">
                    <div class="form-group mt-4">
                        <input class="btn btn-info" type="submit" value="Cadastrar registro" style="float:right;">
                    </div>
                </form>
            </div>
        </div>
    </div>
    <!-- JavaScript, Bootstrap -->
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap\@4.5.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ho+j7jyWK8fNQe+A12Hb8AhRq26LrZ/JpcUGGOn+Y7RsweNrtN/tE3MoK7ZeZDyx" crossorigin="anonymous"></script>
    <!-- Font Awesome -->
    <script src="https://kit.fontawesome.com/a8568f4b07.js" crossorigin="anonymous"></script>
 </body>
</html>
HTML
__END__


