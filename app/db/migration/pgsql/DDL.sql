-- SEQUENCE: public.fund_managers_id_seq

-- DROP SEQUENCE IF EXISTS public.fund_managers_id_seq;

CREATE SEQUENCE IF NOT EXISTS public.fund_managers_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

ALTER SEQUENCE public.fund_managers_id_seq
    OWNER TO aham;

-- SEQUENCE: public.funds_id_seq

-- DROP SEQUENCE IF EXISTS public.funds_id_seq;

CREATE SEQUENCE IF NOT EXISTS public.funds_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

ALTER SEQUENCE public.funds_id_seq
    OWNER TO aham;

-- Table: public.fund_managers

-- DROP TABLE IF EXISTS public.fund_managers;

CREATE TABLE IF NOT EXISTS public.fund_managers
(
    id integer NOT NULL DEFAULT nextval('fund_managers_id_seq'::regclass),
    name character varying(50) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT fund_managers_pkey PRIMARY KEY (id),
    CONSTRAINT uk_fund_manager_name UNIQUE (name)
)

TABLESPACE pg_default;

ALTER SEQUENCE public.fund_managers_id_seq
    OWNED BY public.fund_managers.id;

ALTER TABLE IF EXISTS public.fund_managers
    OWNER to aham;

-- Table: public.funds

-- DROP TABLE IF EXISTS public.funds;

CREATE TABLE IF NOT EXISTS public.funds
(
    id integer NOT NULL DEFAULT nextval('funds_id_seq'::regclass),
    name character varying(50) COLLATE pg_catalog."default" NOT NULL,
    fund_manager_id integer NOT NULL,
    dscp character varying(200) COLLATE pg_catalog."default",
    nav double precision NOT NULL,
    dt_create timestamp without time zone NOT NULL DEFAULT now(),
    performance double precision NOT NULL,
    CONSTRAINT funds_pkey PRIMARY KEY (id),
    CONSTRAINT funds_fund_manager_id_fkey FOREIGN KEY (fund_manager_id)
        REFERENCES public.fund_managers (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER SEQUENCE public.funds_id_seq
    OWNED BY public.funds.id;

ALTER TABLE IF EXISTS public.funds
    OWNER to aham;
-- Index: ix_funds_fund_manager_id

-- DROP INDEX IF EXISTS public.ix_funds_fund_manager_id;

CREATE INDEX IF NOT EXISTS ix_funds_fund_manager_id
    ON public.funds USING btree
    (fund_manager_id ASC NULLS LAST)
    TABLESPACE pg_default;