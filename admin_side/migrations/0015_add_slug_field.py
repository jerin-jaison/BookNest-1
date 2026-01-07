from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('admin_side_product', '0015_previous_migration'),  # REPLACE THIS
    ]

    operations = [
        migrations.RunSQL(
            sql="""
                DO $$ 
                BEGIN
                    IF NOT EXISTS (
                        SELECT 1 FROM information_schema.columns 
                        WHERE table_name='admin_side_product_product' 
                        AND column_name='slug'
                    ) THEN
                        ALTER TABLE admin_side_product_product 
                        ADD COLUMN slug VARCHAR(200) DEFAULT '';
                        
                        -- Generate slugs for existing products
                        UPDATE admin_side_product_product 
                        SET slug = LOWER(REGEXP_REPLACE(
                            REGEXP_REPLACE(title, '[^a-zA-Z0-9\\s-]', '', 'g'), 
                            '\\s+', '-', 'g'
                        )) || '-' || id
                        WHERE slug = '' OR slug IS NULL;
                        
                        -- Create unique index
                        CREATE UNIQUE INDEX admin_side_product_product_slug_idx 
                        ON admin_side_product_product(slug);
                    END IF;
                END $$;
            """,
            reverse_sql="ALTER TABLE admin_side_product_product DROP COLUMN IF EXISTS slug;"
        ),
    ]