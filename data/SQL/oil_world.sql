CREATE TABLE IF NOT EXISTS public.oil_world_prices
(
    "Daily_Prices" character varying COLLATE pg_catalog."default",
    "Palm olein RBD Mal FOB US$" character varying COLLATE pg_catalog."default"
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.oil_world_prices
    OWNER to postgres;