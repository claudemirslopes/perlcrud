#!/usr/bin/perl

use CGI;
use CGI::Carp qw(fatalsToBrowser);
use Encode qw(decode encode);

$BASEAPP = $ENV{HTTP_BASEAPP};

$cgi = new CGI->new;
print $cgi->header(-charset => 'utf-8');

require $BASEAPP."/GLOBAL/cgi-local/modulos/kernel/000.cgi";
use CGI ':standard';
use lib "../controllers"; 

use Testes;

my $id = param('id') if request_method() eq "POST";

my $regEdit = Testes->new();
my $con01 = $regEdit->getById($id);

while (my @data = $con01->fetchrow_array()) {
my $id = $data[0];
my $nome = $data[1];
my $email = $data[2];
my $usuario = $data[3];

print qq~
                    <form action="processa/edita_cadastro.cgi" method="GET">
                         <input type="hidden" value="$id" name="id">
                         <div class="form-group mb-2">
                              <label for="nome">Nome</label>
                              <input type="text" class="form-control" id="nome" name="nome" aria-describedby="nome" value="$nome">
                         </div>
                         <div class="form-group mb-2">
                              <label for="email">E-mail</label>
                              <input type="text" class="form-control" id="email" name="email" aria-describedby="email" value="$email">
                         </div>
                         <div class="form-group mb-2">
                              <label for="usuario">Usuário</label>
                              <input type="text" class="form-control" id="usuario" name="usuario" aria-describedby="usuario" value="$usuario">
                         </div>
                         <div class="form-group mt-4">
                              <input class="btn btn-outline-primary" type="submit" value="Editar registro" style="float:right;">
                         </div>
                    </form>
     ~;

}

