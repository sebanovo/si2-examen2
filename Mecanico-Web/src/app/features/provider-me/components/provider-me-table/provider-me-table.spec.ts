import { ComponentFixture, TestBed } from "@angular/core/testing";

import { ProviderMeTable } from "./provider-me-table";

describe("ProviderMeTable", () => {
	let component: ProviderMeTable;
	let fixture: ComponentFixture<ProviderMeTable>;

	beforeEach(async () => {
		await TestBed.configureTestingModule({
			imports: [ProviderMeTable],
		}).compileComponents();

		fixture = TestBed.createComponent(ProviderMeTable);
		component = fixture.componentInstance;
		await fixture.whenStable();
	});

	it("should create", () => {
		expect(component).toBeTruthy();
	});
});
