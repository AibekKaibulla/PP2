CREATE OR REPLACE FUNCTION insert_multiple_contacts(contacts_list JSONB)
RETURNS TABLE(incorrect_contacts JSONB) AS $$
DECLARE
    contact_data JSONB;
    contact_name TEXT;
    contact_phone TEXT;
BEGIN
    FOR contact_data IN SELECT * FROM jsonb_array_elements(contacts_list)
    LOOP
        contact_name := contact_data ->> 'name';
        contact_phone := contact_data ->> 'phone';

        -- Validate the phone number format here as needed
        IF contact_phone ~ '^[0-9]+$' THEN
            -- Phone number is correct, insert the contact
            INSERT INTO contacts (name, phone) VALUES (contact_name, contact_phone);
        ELSE
            -- Return incorrect contact information
            incorrect_contacts := jsonb_agg(contact_data);
        END IF;
    END LOOP;
    RETURN;
END;
$$ LANGUAGE plpgsql;
