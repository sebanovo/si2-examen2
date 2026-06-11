import { ComponentFixture, TestBed } from "@angular/core/testing";

import { CatalogTable } from "./catalog-table";

describe("CatalogTable", () => {
	let component: CatalogTable;
	let fixture: ComponentFixture<CatalogTable>;

	beforeEach(async () => {
		await TestBed.configureTestingModule({
			imports: [CatalogTable],
		}).compileComponents();

		fixture = TestBed.createComponent(CatalogTable);
		component = fixture.componentInstance;
		await fixture.whenStable();
	});

	it("should create", () => {
		expect(component).toBeTruthy();
	});
});
