import { ComponentFixture, TestBed } from "@angular/core/testing";

import { CatalogEditDialog } from "./catalog-edit-dialog";

describe("CatalogEditDialog", () => {
	let component: CatalogEditDialog;
	let fixture: ComponentFixture<CatalogEditDialog>;

	beforeEach(async () => {
		await TestBed.configureTestingModule({
			imports: [CatalogEditDialog],
		}).compileComponents();

		fixture = TestBed.createComponent(CatalogEditDialog);
		component = fixture.componentInstance;
		await fixture.whenStable();
	});

	it("should create", () => {
		expect(component).toBeTruthy();
	});
});
