
CREATE TABLE public.dim_tempo (
                cod_data VARCHAR(50) NOT NULL,
                desc_data DATE NOT NULL,
                cod_quinzena INTEGER NOT NULL,
                desc_quinzena VARCHAR(255) NOT NULL,
                cod_mes INTEGER NOT NULL,
                desc_mes VARCHAR(255) NOT NULL,
                cod_bimestre INTEGER NOT NULL,
                desc_bimestre VARCHAR(255) NOT NULL,
                cod_trimestre INTEGER NOT NULL,
                desc_trimestre VARCHAR(255) NOT NULL,
                cod_semestre INTEGER NOT NULL,
                desc_semestre VARCHAR(255) NOT NULL,
                cod_ano INTEGER NOT NULL,
                desc_ano VARCHAR(255) NOT NULL,
                CONSTRAINT dim_tempo_pk PRIMARY KEY (cod_data)
);
COMMENT ON COLUMN public.dim_tempo.cod_data IS 'O n�vel folha estabelecido ser� o dia do m�s';
COMMENT ON COLUMN public.dim_tempo.desc_data IS 'data no formato determinado';
COMMENT ON COLUMN public.dim_tempo.desc_quinzena IS 'Descritor da Quinzena';
COMMENT ON COLUMN public.dim_tempo.cod_mes IS 'N�mero do m�s';
COMMENT ON COLUMN public.dim_tempo.desc_mes IS 'M�s por extenso';
COMMENT ON COLUMN public.dim_tempo.cod_bimestre IS 'N�mero do bimestre';
COMMENT ON COLUMN public.dim_tempo.desc_bimestre IS 'Descritor do Bimestre';
COMMENT ON COLUMN public.dim_tempo.cod_trimestre IS 'C�digo do Trimestre';
COMMENT ON COLUMN public.dim_tempo.desc_trimestre IS 'Descritor do trimestre';
COMMENT ON COLUMN public.dim_tempo.cod_semestre IS 'N�mero do Semestre';
COMMENT ON COLUMN public.dim_tempo.desc_semestre IS 'Descritor do Semestre';
COMMENT ON COLUMN public.dim_tempo.cod_ano IS 'N�mero do Ano';
COMMENT ON COLUMN public.dim_tempo.desc_ano IS 'Descritor do Ano';


CREATE TABLE public.dim_turno (
                cod_turno INTEGER NOT NULL,
                desc_turno VARCHAR(255) NOT NULL,
                CONSTRAINT dim_turno_pk PRIMARY KEY (cod_turno)
);
COMMENT ON COLUMN public.dim_turno.cod_turno IS '1, 2 ou 3';
COMMENT ON COLUMN public.dim_turno.desc_turno IS 'Primeiro, segundo, terceiro';


CREATE TABLE public.dim_localizacao (
                cod_maquina VARCHAR NOT NULL,
                desc_maquina VARCHAR(255) NOT NULL,
                cod_centro_custo INTEGER NOT NULL,
                desc_centro_custo VARCHAR(255) NOT NULL,
                cod_setor VARCHAR(50) NOT NULL,
                desc_setor VARCHAR(255) NOT NULL,
                cod_tipo_maquina VARCHAR(50) NOT NULL,
                desc_tipo_maquina VARCHAR(255) NOT NULL,
                CONSTRAINT dim_localizacao_pk PRIMARY KEY (cod_maquina)
);
COMMENT ON TABLE public.dim_localizacao IS 'Tabela da Dimens�o Localiza��o';
COMMENT ON COLUMN public.dim_localizacao.cod_maquina IS 'id m�quina = TAG da m�quina cadastrado no SAP';
COMMENT ON COLUMN public.dim_localizacao.cod_centro_custo IS 'ID do centro de custo � o c�digo num�rico do sistema SAP';
COMMENT ON COLUMN public.dim_localizacao.desc_centro_custo IS 'Descritor do Centro de Custos da tabela de contros de custos';
COMMENT ON COLUMN public.dim_localizacao.cod_setor IS 'codifica��o do pr�dio';
COMMENT ON COLUMN public.dim_localizacao.desc_setor IS 'Nome do setor';
COMMENT ON COLUMN public.dim_localizacao.cod_tipo_maquina IS '3 primeiras letras do TAG';
COMMENT ON COLUMN public.dim_localizacao.desc_tipo_maquina IS 'Descritor do tipo de m�quina';


CREATE TABLE public.fato_2 (
                cod_maquina VARCHAR NOT NULL,
                cod_turno INTEGER NOT NULL,
                cod_data VARCHAR(50) NOT NULL,
                duracao_manutencao TIME NOT NULL,
                n_preventiva INTEGER NOT NULL,
                n_corretiva INTEGER NOT NULL,
                horas_trabalhadas TIME NOT NULL,
                n_quebras INTEGER NOT NULL,
                CONSTRAINT fato_2_pk PRIMARY KEY (cod_maquina, cod_turno, cod_data)
);
COMMENT ON TABLE public.fato_2 IS 'Tabela de Fato 2';
COMMENT ON COLUMN public.fato_2.cod_maquina IS 'id m�quina = TAG da m�quina cadastrado no SAP';
COMMENT ON COLUMN public.fato_2.cod_turno IS '1, 2 ou 3';
COMMENT ON COLUMN public.fato_2.cod_data IS 'O n�vel folha estabelecido ser� o dia do m�s';
COMMENT ON COLUMN public.fato_2.duracao_manutencao IS 'Dura��o da manuten��o';
COMMENT ON COLUMN public.fato_2.n_preventiva IS 'Quantidade de Preventivas';
COMMENT ON COLUMN public.fato_2.n_corretiva IS 'Quantidade de corretivas';
COMMENT ON COLUMN public.fato_2.horas_trabalhadas IS 'Horas de Trabalho da M�quina';
COMMENT ON COLUMN public.fato_2.n_quebras IS 'Quantidade de Quebras';


CREATE TABLE public.fato_1 (
                cod_data VARCHAR(50) NOT NULL,
                cod_maquina VARCHAR NOT NULL,
                custo_manutencao DOUBLE PRECISION NOT NULL,
                n_calibracoes INTEGER NOT NULL,
                custo_calibracao DOUBLE PRECISION NOT NULL,
                n_itens_estoque INTEGER NOT NULL,
                valor_estoque DOUBLE PRECISION NOT NULL,
                meta_custos DOUBLE PRECISION NOT NULL,
                custo_fixo_manutencao DOUBLE PRECISION NOT NULL,
                custo_variavel_manutencao DOUBLE PRECISION NOT NULL,
                meta_valor_estoque DOUBLE PRECISION NOT NULL,
                CONSTRAINT fato_1_pk PRIMARY KEY (cod_data, cod_maquina)
);
COMMENT ON TABLE public.fato_1 IS 'Tabela Fato 1';
COMMENT ON COLUMN public.fato_1.cod_data IS 'O n�vel folha estabelecido ser� o dia do m�s';
COMMENT ON COLUMN public.fato_1.cod_maquina IS 'id m�quina = TAG da m�quina cadastrado no SAP';
COMMENT ON COLUMN public.fato_1.custo_manutencao IS 'Custo de manuten��o';
COMMENT ON COLUMN public.fato_1.n_calibracoes IS 'N�mero de calibra��es';
COMMENT ON COLUMN public.fato_1.custo_calibracao IS 'Custos com a calibra��o';
COMMENT ON COLUMN public.fato_1.n_itens_estoque IS 'N�mero de itens no estoque';
COMMENT ON COLUMN public.fato_1.valor_estoque IS 'Valor dos itens do estoque';
COMMENT ON COLUMN public.fato_1.meta_custos IS 'Meta dos Custos de Manuten��o';
COMMENT ON COLUMN public.fato_1.custo_fixo_manutencao IS 'Custos fixos de manuten��o';
COMMENT ON COLUMN public.fato_1.custo_variavel_manutencao IS 'Custo vari�vel de manuten��o';
COMMENT ON COLUMN public.fato_1.meta_valor_estoque IS 'Meta do valor do estoque';


ALTER TABLE public.fato_1 ADD CONSTRAINT dim_tempo_fato_1_fk
FOREIGN KEY (cod_data)
REFERENCES public.dim_tempo (cod_data)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.fato_2 ADD CONSTRAINT dim_tempo_fato_2_fk
FOREIGN KEY (cod_data)
REFERENCES public.dim_tempo (cod_data)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.fato_2 ADD CONSTRAINT dim_turno_fato_2_fk
FOREIGN KEY (cod_turno)
REFERENCES public.dim_turno (cod_turno)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.fato_1 ADD CONSTRAINT dim_localizacao_fato_1_fk
FOREIGN KEY (cod_maquina)
REFERENCES public.dim_localizacao (cod_maquina)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.fato_2 ADD CONSTRAINT dim_localizacao_fato_2_fk
FOREIGN KEY (cod_maquina)
REFERENCES public.dim_localizacao (cod_maquina)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;
