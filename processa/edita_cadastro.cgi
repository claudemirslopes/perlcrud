#!/usr/bin/perl

use strict;
use warnings;
use CGI::Carp qw(fatalsToBrowser warningsToBrowser);
use CGI ':standard';
use lib "../controllers"; 
use Data::Dumper;
use Testes;

my $cgi = new CGI->new;
print $cgi->redirect('../index.cgi');

my $id = param('id');
my $nome = param('nome');
my $email = param('email');
my $usuario = param('usuario');

my $regEdit = Testes->new();
$regEdit->update($id, $nome, $email, $usuario);

