#!/usr/bin/perl

use CGI;
use CGI::Carp qw(fatalsToBrowser);
use Encode qw(decode encode);

$BASEAPP = $ENV{HTTP_BASEAPP};

$cgi = new CGI->new;

require $BASEAPP."/GLOBAL/cgi-local/modulos/kernel/000.cgi";
use CGI ':standard';
use lib "../controllers"; 

use Testes;

my $id = param('del_id');

my $regDel = Testes->new();
$regDel->deleteById($id);

print $cgi->redirect('../index.cgi');



