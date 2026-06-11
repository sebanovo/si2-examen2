import { ComponentFixture, TestBed } from "@angular/core/testing";

import { CatalogDetailDialog } from "./catalog-detail-dialog";

describe("CatalogDetailDialog", () => {
	let component: CatalogDetailDialog;
	let fixture: ComponentFixture<CatalogDetailDialog>;

	beforeEach(async () => {
		await TestBed.configureTestingModule({
			imports: [CatalogDetailDialog],
		}).compileComponents();

		fixture = TestBed.createComponent(CatalogDetailDialog);
		component = fixture.componentInstance;
		await fixture.whenStable();
	});

	it("should create", () => {
		expect(component).toBeTruthy();
	});
});
