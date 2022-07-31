CREATE TABLE IF NOT EXISTS public.crop_efficiency
(
    "Crop" character varying COLLATE pg_catalog."default",
    "Year" character varying COLLATE pg_catalog."default",
    "area needed to meet global vegetable oil demand" character varying COLLATE pg_catalog."default"
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.crop_efficiency
    OWNER to postgres;