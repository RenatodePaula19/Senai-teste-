create database if not exists bd_chamados;

use bd_chamados;

create table if not exists chamados(id integer primary key auto_increment,
									nome varchar(45) not null,
                                    local varchar(45) not null,
                                    setor varchar(200) not null,
                                    data_abertura datetime,
                                    comentario varchar(255) not null,
                                    status boolean default true);

                                							
alter table chamados add column data_fechamento datetime;

