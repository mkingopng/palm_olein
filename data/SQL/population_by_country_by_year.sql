CREATE TABLE IF NOT EXISTS public.population_by_country_by_year
(
    country_name character varying COLLATE pg_catalog."default",
    year character varying COLLATE pg_catalog."default",
    population character varying COLLATE pg_catalog."default"
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.population_by_country_by_year
    OWNER to postgres;