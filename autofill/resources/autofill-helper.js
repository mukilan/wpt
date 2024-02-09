async function save_address_fields(address_fields) {
  test_driver.save_address_to_autofill(address_fields);

  let count = 10;
  while (count > 0) {
    if (await test_driver.expect_address_in_autofill(address_fields)) {
      break;
    }
    await new Promise(r=>step_timeout(r, 10));
    --count;
  }
}
