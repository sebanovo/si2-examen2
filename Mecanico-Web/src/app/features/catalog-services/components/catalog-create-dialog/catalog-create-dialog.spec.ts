import { ComponentFixture, TestBed } from "@angular/core/testing";

import { CatalogCreateDialog } from "./catalog-create-dialog";

describe("CatalogCreateDialog", () => {
	let component: CatalogCreateDialog;
	let fixture: ComponentFixture<CatalogCreateDialog>;

	beforeEach(async () => {
		await TestBed.configureTestingModule({
			imports: [CatalogCreateDialog],
		}).compileComponents();

		fixture = TestBed.createComponent(CatalogCreateDialog);
		component = fixture.componentInstance;
		await fixture.whenStable();
	});

	it("should create", () => {
		expect(component).toBeTruthy();
	});
});
