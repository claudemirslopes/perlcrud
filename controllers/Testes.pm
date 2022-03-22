package Testes;

use warnings;
use DBI;
use lib ".";

$BASEAPP = $ENV{HTTP_BASEAPP};
$cgi = new CGI->new;

require $BASEAPP."/GLOBAL/cgi-local/modulos/kernel/000.cgi";

sub new {
   my $class = shift;
   my $self = {};
    bless $self, $class;
    return $self;
}

sub getId {
    my ($self) = @_;
    return $self->{id};
}

sub setNome {
    my ($self,$nome) = @_;
    $self->{nome} = $nome;
}

sub getNome {
    my ($self) = @_;
    return $self->{nome};
}

sub setEmail {
    my ($self,$email) = @_;
    $self->{email} = $email;
}

sub getEmail {
    my ($self) = @_;
    return $self->{email};

}

sub setUsuario {
    my ($self,$usuario) = @_;
    $self->{usuario} = $usuario;
}

sub getUsuario {
    my ($self) = @_;
    return $self->{usuario};

}

sub setSenha {
    my ($self,$senha) = @_;
    $self->{senha} = $senha;
}

sub getSenha {
    my ($self) = @_;
    return $self->{senha};
}

sub getAll {
    my ($self) = @_;
    my $query = "SELECT id, nome, email, usuario, senha, criado FROM _noob_teste";
    my $con01 = $conexao->prepare($query);
    $con01->execute();
    return $con01;    

}

#Listar do banco de dados
sub getById {
    my ($self, $id) = @_;
    my $sql = "SELECT id, nome, email, usuario, senha, criado FROM _noob_teste WHERE id=$id";
    my $con01 = $conexao->prepare($sql);
    $con01->execute();
    return $con01;
}
    
#Salvar no banco de dados
sub save {
    my ($self, $nome, $email, $usuario, $senha) = @_;
    my $sql = "INSERT INTO _noob_teste (nome, email, usuario, senha) VALUES(?, ?, ?, ?)";
    my $con01 = $conexao->prepare($sql);
    $con01->execute($nome, $email, $usuario, $senha);

    if($DBI::errstr ne undef){
        
        return $DBI::errstr;
    }
}

#Atualizações
sub update {
    my ($self, $id, $nome, $email, $usuario) = @_;
    my $sql = "UPDATE _noob_teste SET id='$id', nome='$nome', email='$email', usuario='$usuario' WHERE id='$id'";
    my $con01 = $conexao->prepare($sql);
    $con01->execute();

    if($DBI::errstr ne undef){
        
        return $DBI::errstr;
    }
}

#Exclusões
sub deleteById {
    my ($self, $id) = @_;
    my $sql = "DELETE FROM _noob_teste WHERE id=$id";
    my $con01 = $conexao->prepare($sql);
    $con01->execute();
}


1;

